from datetime import timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
from django.core.cache import cache
from django.db.models import Q

from ISSEASuiviEnquete.settings import API_URL, API_USERNAME, API_PASSWORD
from accounts.models import CustomUser
from survey_solutions_api_client import AuthenticatedClient
from survey_solutions_api_client.api.assignments import get_api_v1_assignments
from survey_solutions_api_client.api.interviews import (
    get_api_v1_interviews_id,
    get_api_v1_interviews_id_stats
)
from survey_solutions_api_client.api.questionnaires import (
    get_api_v1_questionnaires,
    get_api_v1_questionnaires_id_version_interviews
)
from survey_solutions_api_client.models import AssignmentsListView

pio.templates.default = "plotly_white"


def get_time_intervals(start_datetime, end_datetime):
    if start_datetime > end_datetime:
        raise ValueError("Start datetime should be older than end datetime")

    time_intervals = []

    current_time = start_datetime
    while current_time <= end_datetime:
        time_intervals.append((current_time.hour, current_time.minute))
        current_time += timedelta(minutes=1)

    return time_intervals


class MetricsAndPlots:
    def __init__(self, user_login: str):
        self.user: CustomUser = CustomUser.objects.get(login=user_login)
        self.client: AuthenticatedClient = AuthenticatedClient(
            base_url=API_URL + self.user.workspace,
            username=API_USERNAME + self.user.workspace,
            password=API_PASSWORD
        )

    @property
    def user_assignments_detailed(self):
        # Cache assignments data for a specific user and timeframe (adjust timeout as needed)
        cache_key = f"user_assignments_{self.user.login}"
        assignments_data = cache.get(cache_key)
        if assignments_data is None:
            assignments_data = get_api_v1_assignments.sync(client=self.client, responsible=self.user.login)
            cache.set(cache_key, assignments_data, timeout=300)
        return assignments_data

    @property
    def user_questionnaires(self):
        cache_key = "user_questionnaires"
        questionnaires_data = cache.get(cache_key)
        if questionnaires_data is None:
            questionnaires_data = get_api_v1_questionnaires.sync(client=self.client).questionnaires
            cache.set(cache_key, questionnaires_data, timeout=300)
        return questionnaires_data

    @property
    def user_interviews(self):
        cache_key = f"user_interviews_{self.user.login}"
        all_interviews = cache.get(cache_key)
        if all_interviews is None:
            all_questionnaires = [(quest.questionnaire_id, quest.version) for quest in self.user_questionnaires]
            all_interviews = {}
            for iden, version in all_questionnaires:
                off = 1
                interviews_qver = get_api_v1_questionnaires_id_version_interviews.sync(
                    iden, version, client=self.client, offset=off).interviews
                while len(interviews_qver) > 0:
                    for interview in interviews_qver:
                        if (interview.interview_id not in all_interviews) and (
                                interview.responsible_name == self.user.login):
                            all_interviews[interview.interview_id] = [interview.last_entry_date,
                                                                      interview.featured_questions[0].answer,
                                                                      interview.featured_questions[1].answer,
                                                                      interview.featured_questions[2].answer]
                    interviews_qver = get_api_v1_questionnaires_id_version_interviews.sync(
                        iden, version, client=self.client, offset=off).interviews
                    off += 1
            cache.set(cache_key, all_interviews, timeout=300)
        return all_interviews

    @property
    def user_interviews_id(self):
        return self.user_interviews.keys()

    @property
    def user_interviews_answers(self):
        return list(get_api_v1_interviews_id.sync(item, client=self.client).answers
                    for item in self.user_interviews_id)

    @property
    def user_interviews_stats(self):
        return list(get_api_v1_interviews_id_stats.sync(id=item, client=self.client)
                    for item in self.user_interviews_id)

    @property
    def user_dash_data(self) -> pd.DataFrame:
        cache_key = f"user_dash_data_{self.user.login}"
        dash_data = cache.get(cache_key)
        if dash_data is None:
            data = list(self.user_interviews.values())
            durations = list(item.interview_duration for item in self.user_interviews_stats)
            f_status = lambda x: x[-2].answer if x[-3].answer in ['Partiellement rempli', 'Partially filled'] else x[
                -3].answer
            status = list(f_status(answer) for answer in self.user_interviews_answers)
            survey_solutions_status = list(item.status for item in self.user_interviews_stats)
            appreciation = list(i[-1].answer for i in self.user_interviews_answers)
            for idx, item in enumerate(durations):
                data[idx].append(item)
            for idx, item in enumerate(status):
                data[idx].append(item)
            for idx, item in enumerate(survey_solutions_status):
                data[idx].append(item)
            for idx, item in enumerate(appreciation):
                data[idx].append(item)

            dash_data = pd.DataFrame(data, columns=[
                'dates', 'arrondissement', 'enumeration_area', 'household_eanumber',
                'durations', 'status', 'survey_solutions_status', 'appreciation'
            ])

            dash_data.insert(1, column='date', value=dash_data.dates.dt.date)

            dash_data = dash_data.sort_values(
                by=['dates', 'arrondissement', 'enumeration_area', 'household_eanumber']
            )

            map_status = {
                'Completely filled': 'Entièrement rempli',
                'Refusal': 'Refus',
                'Dwelling destroyed/not found': 'Logement détruit/non trouvé',
                'Long-term absence': 'Absence de longue durée'
            }

            dash_data.status = dash_data.status.apply(lambda x: map_status[x] if x in map_status else x)

            cache.set(cache_key, dash_data, timeout=300)
        return dash_data

    def get_01_workload(self):
        return self.user_assignments_detailed.total_count

    def get_02_completed_interviews_number(self):
        completed = self.user_dash_data.status.isin(['Entièrement rempli']).sum()
        rejected = self.user_dash_data.survey_solutions_status.isin(
            ['RejectedByHeadquarters', 'RejectedBySupervisor', 'Deleted']).sum()
        return completed - rejected

    def get_03_completed_interviews_percentage(self):
        return f'{round(100 * self.get_02_completed_interviews_number() / self.get_01_workload())}%'

    def get_04_completed_interviews_net_percentage(self):
        nb_partial = self.user_dash_data.status.isin(['Partiellement rempli', 'Partially filled']).sum()
        return f'{round(100 * self.get_02_completed_interviews_number() / (self.get_01_workload() - nb_partial))}%'

    def plot_01_completed_interviews_number_per_day(self):
        data = self.user_dash_data['date'].value_counts().sort_index()
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data.values,
                mode='lines+markers',
            )
        )
        fig.update_layout(
            height=300,
            xaxis_title='Date',
            yaxis_title='Enquêtés',
            margin=dict(l=0, r=0, t=0, b=0)
        )
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_02_completed_interviews_cumulative_number(self):
        data = self.user_dash_data['date'].value_counts().sort_index().cumsum() / self.get_01_workload()
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data.values,
                mode='lines+markers',
            )
        )
        fig.update_layout(
            height=300,
            xaxis_title='Date',
            yaxis_title='% Enquêtés',
            margin=dict(l=0, r=0, t=0, b=0)
        )
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_03_visited_households_status(self):
        fig = px.pie(
            self.user_dash_data,
            names='status',
            hole=.3
        )
        fig.update_layout(
            height=300,
            margin=dict(l=20, r=2, t=0, b=0),
            legend=dict(
                y=0.5,
                x=0.02
            )
        )
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_04_visited_households_status_per_ea(self):
        data = self.user_dash_data.groupby(['enumeration_area', 'status']).size().reset_index(name='count')
        fig = px.bar(
            data,
            x='enumeration_area',
            y='count',
            color='status',
            barmode='group',
            labels={'enumeration_area': 'No ZD', 'count': 'Effectifs'}
        )
        fig.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=0, b=30),
            legend=dict(
                xanchor='left',
                y=0.5,
            )
        )
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_05_completed_interviews_number_per_day_and_ea(self):
        data = self.user_dash_data[['enumeration_area', 'date']].value_counts().sort_index()

        fig = go.Figure()
        for ea in sorted(data.index.get_level_values('enumeration_area').unique()):
            sub_data = data[ea]
            fig.add_trace(
                go.Scatter(
                    x=sub_data.index,
                    y=sub_data.values,
                    mode='lines+markers',
                    name='ZD No' + str(ea)
                )
            )

        fig.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=0, b=30),
            legend=dict(
                xanchor='left',
                y=0.5,
            )
        )

        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_06_completed_interviews_cumulative_number_per_ea(self):
        data = self.user_dash_data[['enumeration_area', 'date']].value_counts().sort_index()

        fig = go.Figure()
        for ea in sorted(data.index.get_level_values('enumeration_area').unique()):
            sub_data = data[ea].cumsum()
            fig.add_trace(
                go.Scatter(
                    x=sub_data.index,
                    y=sub_data.values,
                    mode='lines+markers',
                    name='ZD No' + str(ea)
                )
            )

        fig.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=0, b=30),
            legend=dict(
                xanchor='left',
                y=0.5,
            )
        )

        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def plot_spatial_progression(self):
        pass


class SupervisorMetricsAndPlots(MetricsAndPlots):
    def __init__(self, user_login: str):
        super().__init__(user_login)

    @property
    def get_team_members(self):
        return CustomUser.objects.filter(Q(supervisor=self.user.login))

    def get_team_member_data(self, method_name):
        team_member_data = []
        for member in self.get_team_members:
            team_member_data.append(getattr(MetricsAndPlots(user_login=member.login), method_name)())
        return team_member_data

    @property
    def user_dash_data(self) -> pd.DataFrame:
        team_member_logins = []
        team_member_dataframes = []
        for member in self.get_team_members:
            member_df = MetricsAndPlots(user_login=member.login).user_dash_data
            team_member_logins += [member.login] * member_df.shape[0]
            team_member_dataframes.append(member_df)

        data = pd.concat(team_member_dataframes)
        data['interviewer'] = team_member_logins

        return data

    def get_01_workload(self):
        team_member_workloads = self.get_team_member_data("get_01_workload")
        return sum(team_member_workloads)

    def get_02_completed_interviews_number(self):
        team_completed_interviews_number = self.get_team_member_data("get_02_completed_interviews_number")
        return sum(team_completed_interviews_number)

    # Nombre de ménages enquêtés par jour et par ZD
    def plot_03_visited_households_status(self):
        return super().plot_05_completed_interviews_number_per_day_and_ea()

    # Pourcentage cumulé du nombre de ménages enquêtés par jour et par ZD
    def plot_04_visited_households_status_per_ea(self):
        return super().plot_06_completed_interviews_cumulative_number_per_ea()

    # Nombre de ménages enquêtés par jour et par enquêteur
    def plot_05_completed_interviews_number_per_day_and_ea(self):
        data = self.user_dash_data[['interviewer', 'date']].value_counts().sort_index()

        fig = go.Figure()
        for interviewer in sorted(data.index.get_level_values('interviewer').unique()):
            sub_data = data[interviewer]
            fig.add_trace(
                go.Scatter(
                    x=sub_data.index,
                    y=sub_data.values,
                    mode='lines+markers',
                    name='Enquêteur No ' + str(interviewer)
                )
            )

        fig.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=0, b=30),
            legend=dict(
                xanchor='left',
                y=0.5,
            )
        )

        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Cumul du nombre de ménages enquêtés par jour et par enquêteur
    def plot_06_completed_interviews_cumulative_number_per_ea(self):
        data = self.user_dash_data[['interviewer', 'date']].value_counts().sort_index()

        fig = go.Figure()
        for interviewer in sorted(data.index.get_level_values('interviewer').unique()):
            sub_data = data[interviewer].cumsum()
            fig.add_trace(
                go.Scatter(
                    x=sub_data.index,
                    y=sub_data.values,
                    mode='lines+markers',
                    name='Enquêteur No ' + str(interviewer)
                )
            )

        fig.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=0, b=30),
            legend=dict(
                xanchor='left',
                y=0.5,
            )
        )

        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Statut des ménages visités par ZD
    def plot_07_completed_interviews_number_per_day_and_interviewer(self):
        return super().plot_04_visited_households_status_per_ea()

    # Statut des ménages visités par enquêteur
    def plot_08_completed_interviews_cumulative_number_per_interviewer(self):
        data = self.user_dash_data.groupby(['interviewer', 'status']).size().reset_index(name='count')
        fig = px.bar(
            data,
            x='interviewer',
            y='count',
            color='status',
            barmode='group',
            labels={'interviewer': 'No Enquêteur', 'count': 'Effectifs'}
        )
        fig.update_layout(
            height=300,
            margin=dict(l=0, r=0, t=0, b=30),
            legend=dict(
                xanchor='left',
                y=0.5,
            )
        )
        return fig.to_html(full_html=False, include_plotlyjs='cdn')

    def get_05_interviews_duration_mean(self, selected_interviewer):
        interviewer_data = self.user_dash_data[self.user_dash_data.interviewer.eq(selected_interviewer)]
        total_seconds = pd.to_timedelta(interviewer_data['durations']).dt.total_seconds().mean()

        if pd.isna(total_seconds):
            return "00:00"

        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        return f"{minutes:02}:{seconds:02}"

    def get_06_interviews_duration_total(self, selected_interviewer):
        interviewer_data = self.user_dash_data[self.user_dash_data.interviewer.eq(selected_interviewer)]
        total_seconds = pd.to_timedelta(interviewer_data['durations']).dt.total_seconds().sum()

        if pd.isna(total_seconds):
            return "00:00"

        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        return f"{minutes:02}:{seconds:02}"

    def get_07_surveyed_households_without_gps_number(self):
        pass

    def get_08_risk_interviewer_probability(self):
        pass

    # Diagramme d'activité
    def plot_10_activity_diagram(self, selected_interviewer):
        interviewer_data = self.user_dash_data[self.user_dash_data.interviewer.eq(selected_interviewer)][
            ['dates', 'durations']]
        interviewer_data.rename(columns={'dates': 'end_date'}, inplace=True)
        # interviewer_data['end_date'] = pd.to_datetime(interviewer_data['end_date'])
        interviewer_data['durations'] = pd.to_timedelta(interviewer_data['durations'])
        interviewer_data['start_date'] = interviewer_data['end_date'] - interviewer_data['durations']
        interviewer_data.drop(columns='durations', inplace=True)

        activity_grid = np.zeros((24, 60))

        # Fill the activity grid
        for index, row in interviewer_data.iterrows():
            start = row['start_date']
            end = row['end_date']
            all_times = get_time_intervals(start, end)
            for heure, minutes in all_times:
                activity_grid[heure, minutes] = 1

        fig = go.Figure(data=go.Heatmap(
            z=activity_grid,
            x=list(range(60)),
            y=list(range(24)),
            colorscale=[
                [0, 'black'],
                [1, 'green']
            ],
            zmin=0,
            zmax=1,
            showscale=False,
            hovertemplate="Heure: %{y}:%{x}<br>Intensité d'activité: %{z}",
        ))

        # Update layout
        fig.update_layout(
            xaxis=dict(title='Minutes', tickmode='array', tickvals=list(range(0, 60, 1))),
            yaxis=dict(title='Heures', tickmode='array', tickvals=list(range(0, 24, 1))),
            plot_bgcolor='white',
            margin=dict(l=0, r=0, t=0, b=0)
        )

    # Durée d’administration du questionnaire par enquêteurs
    def plot_11_interviews_duration(self):
        pass


class HeadquatersMetricsAndPlots(MetricsAndPlots):
    def plot_07_visited_households_status_cumulative(self):
        pass

    def plot_08_visited_households_status_per_controller(self):
        pass

    def plot_09_completed_interviews_number_per_day_and_controller(self):
        pass

    def plot_10_completed_interviews_cumulative_number_per_controller(self):
        pass
