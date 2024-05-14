from turtle import width

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from ISSEASuiviEnquete.settings import API_URL, API_USERNAME, API_PASSWORD
from accounts.models import CustomUser
from survey_solutions_api_client import AuthenticatedClient
from survey_solutions_api_client.api.assignments import get_api_v1_assignments
from survey_solutions_api_client.api.interviews import (
    get_api_v1_interviews,
    get_api_v1_interviews_id,
    get_api_v1_interviews_id_stats
)
from survey_solutions_api_client.models import AssignmentsListView


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
        data: AssignmentsListView = get_api_v1_assignments.sync(
            client=self.client,
            responsible=self.user.login,
        )
        return data

    @property
    def user_assignments(self):
        data = self.user_assignments_detailed
        return data.assignments

    @property
    def user_interviews(self):
        all_interviews = get_api_v1_interviews.sync(client=self.client)
        user_interviews = list(interview for interview in all_interviews.interviews
                               if interview.responsible_name == self.user.login)
        return user_interviews

    @property
    def user_interviews_id(self):
        return list(i.interview_id for i in self.user_interviews)

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
        data = [
            [item.last_entry_date,
             item.featured_questions[0].answer,
             item.featured_questions[1].answer,
             item.featured_questions[2].answer]
            for item in self.user_interviews
        ]
        durations = list(item.interview_duration for item in self.user_interviews_stats)
        f_status = lambda x: x[-3].answer if x[-4].answer in ['Partiellement rempli', 'Partially filled'] else x[
            -4].answer
        status = list(f_status(answer) for answer in self.user_interviews_answers)
        appreciation = list(i[-1].answer for i in self.user_interviews_answers)
        for idx, item in enumerate(durations):
            data[idx].append(item)
        for idx, item in enumerate(status):
            data[idx].append(item)
        for idx, item in enumerate(appreciation):
            data[idx].append(item)

        dash_data = pd.DataFrame(data, columns=[
            'dates', 'arrondissement', 'enumeration_area', 'household_eanumber',
            'durations', 'status', 'appreciation'
        ])

        dash_data.insert(1, column='date', value=dash_data.dates.dt.date)
        # Sort and set index in a single step using chained methods
        return dash_data.sort_values(
            by=['dates', 'arrondissement', 'enumeration_area', 'household_eanumber']
        )

    def get_01_workload(self):
        return sum(item.quantity for item in self.user_assignments)

    def get_02_completed_interviews_number(self):
        return sum(item.interviews_count for item in self.user_assignments)

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
        pass

    def plot_03_visited_households_status(self):
        pass

    def plot_04_visited_households_status_per_ea(self):
        pass

    def plot_05_completed_interviews_number_per_day_and_ea(self):
        pass

    def plot_06_completed_interviews_cumulative_number_per_ea(self):
        pass

    def plot_spatial_progression(self):
        pass


class SupervisorMetricsAndPlots(MetricsAndPlots):
    def plot_07_completed_interviews_number_per_day_and_interviewer(self):
        pass

    def plot_08_completed_interviews_cumulative_number_per_interviewer(self):
        pass

    def plot_09_visited_households_status_per_interviewer(self):
        pass

    def get_05_interviews_duration_mean(self):
        pass

    def get_06_interviews_duration_total(self):
        pass

    def get_07_surveyed_households_without_gps_number(self):
        pass

    def get_08_risk_interviewer_probability(self):
        pass

    def plot_10_activity_diagram(self):
        pass

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
