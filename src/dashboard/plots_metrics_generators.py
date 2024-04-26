from ISSEASuiviEnquete.settings import API_URL, API_USERNAME, API_PASSWORD
from accounts.models import CustomUser
from survey_solutions_api_client import AuthenticatedClient
from survey_solutions_api_client.api.assignments import get_api_v1_assignments
from survey_solutions_api_client.api.users import get_api_v1_users_id
from survey_solutions_api_client.models import AssignmentsListView, UserApiDetails


class MetricsAndPlots:
    def __init__(self, user_login: str):
        self.user: CustomUser = CustomUser.objects.get(login=user_login)
    #     self.client: AuthenticatedClient = AuthenticatedClient(
    #         base_url=API_URL,
    #         username=API_USERNAME,
    #         password=API_PASSWORD
    #     )
    #
    # @property
    # async def user_details(self):
    #     data: UserApiDetails = await get_api_v1_users_id.sync(
    #         id=self.user.login,
    #         client=self.client
    #     )
    #     return data
    #
    # @property
    # def user_assigments_detailed(self):
    #     data: AssignmentsListView = get_api_v1_assignments.sync(
    #         client=self.client,
    #         responsible=self.user.login,
    #     )
    #     return data
    #
    # @property
    # def user_assigments(self):
    #     data: AssignmentsListView = self.user_assigments_detailed
    #     return data.assignments
    #
    # @property
    # def user_questionnaires_id(self):
    #     user_assignments = self.user_assigments
    #     return list(item.questionnaire_id for item in user_assignments)

    def get_01_workload(self):
        return 20
        # user_assignments = self.user_assigments
        # return sum(item.quantity for item in user_assignments)

    def get_02_completed_interviews_number(self):
        # get_api_v1_interviews
        return 10

    def get_03_completed_interviews_percentage(self):
        return '50%'

    def get_04_completed_interviews_net_percentage(self):
        return '70%'

    def plot_01_completed_interviews_number_per_day(self):
        pass

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
