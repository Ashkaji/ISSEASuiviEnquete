import pickle

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ISSEASuiviEnquete.settings import API_USERNAME, API_PASSWORD, API_URL


class MetricsAndPlots:
    def __init__(self, user_login):
        self.user_login = user_login


class InterviewerMetricsAndPlots:
    def __init__(self, user_login, *args, **kwargs):
        self.user_login = user_login

    def get_01_workload(self):
        pass

    def get_02_completed_interviews_number(self):
        pass

    def get_03_completed_interviews_percentage(self):
        pass

    def get_04_completed_interviews_net_percentage(self):
        pass

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


class ControllerMetricsAndPlots(InterviewerMetricsAndPlots):
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


class SupervisorMetricsAndPlots(InterviewerMetricsAndPlots):
    def plot_07_visited_households_status_cumulative(self):
        pass

    def plot_08_visited_households_status_per_controller(self):
        pass

    def plot_09_completed_interviews_number_per_day_and_controller(self):
        pass

    def plot_10_completed_interviews_cumulative_number_per_controller(self):
        pass


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def current_user(self):
        return self.request.user

    @property
    def current_user_group(self):
        user_groups = self.current_user.groups.all()
        if user_groups:
            return user_groups[0].name
        else:
            return 'base'

    @property
    def header_message(self, *args, **kwargs):
        principal_message = """<h1>Bienvenu sur votre tableau de bord!</h1>
        <p>Vous trouverez toutes les informations dont
        vous avez besoin pour une meilleure collecte"""
        personalised_msg = {
            'Supervisors': ' dans votre zone</p>',
            'Interviewers': '</p>',
        }
        _header_msg = 'Nothing to show'
        if self.current_user_group in personalised_msg.keys():
            _header_msg = principal_message + personalised_msg.get(self.current_user_group)

        return _header_msg

    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        return f'dashboard/{self.current_user_group}-dash.html'

    def get_sections_layout(self, *args, **kwargs):
        section_data_file = f'dashboard/rendering/{self.current_user_group}.pickle'
        try:
            with open(section_data_file, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    #
    # def get_metrics_and_plots_generator(self):
    #     match self.current_user_group:
    #         case 'Interviewers':
    #             return InterviewerMetricsAndPlots(user_login=self.request.user.username)
    #         case 'Controllers':
    #             return ControllerMetricsAndPlots(user_login=self.request.user.username)
    #         case _:
    #             return SupervisorMetricsAndPlots(user_login=self.request.user.username)

    @staticmethod
    def get_metrics_and_plots_method_names(cls_instance):
        all_methods = dir(cls_instance)
        metrics = [c for c in all_methods if c.split('_')[0] == 'get']
        plots = [c for c in all_methods if c.split('_')[0] == 'plot']
        return dict(metrics=metrics, plots=plots)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.template_name = self.get_template_names()

        context['header_message'] = self.header_message
        section_to_render = self.get_sections_layout()

        # metrics_and_plots = self.get_metrics_and_plots_generator()

        # methods = self.get_metrics_and_plots_method_names(metrics_and_plots)['metrics']
        # for idx, section in enumerate(section_to_render):
        #     if section['section_type'] == 'metrics':
        #         for bloc in section['section_data']:
        #             method = getattr(metrics_and_plots, methods[idx])
        #             bloc['value'] = method()

        # for section in section_to_render:
        #     if section['section_type'] == 'plots':
        #         for bloc in section['section_data']:
        #             bloc['plot'] = fig.to_html(full_html=False, include_plotlyjs='cdn', include_mathjax=False, )

        context['sections'] = section_to_render

        return context
