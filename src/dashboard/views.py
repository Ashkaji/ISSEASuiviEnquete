import inspect
import pickle
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import TemplateView
from accounts.models import CustomUser
from dashboard.forms import InterviewerSelectForm
from dashboard.plots_metrics_generators import MetricsAndPlots, SupervisorMetricsAndPlots, HeadquatersMetricsAndPlots


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def current_user(self):
        return self.request.user

    @property
    def current_user_group(self):
        if user_groups := self.current_user.groups.all():
            return user_groups[0].name
        else:
            return 'base'

    def dispatch(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return self.handle_ajax(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        return f'dashboard/{self.current_user_group}-dash.html'

    def get_sections_skeleton(self, *args, **kwargs):
        section_data_file = f'dashboard/rendering/{self.current_user_group}.pickle'
        try:
            with open(section_data_file, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def get_metrics_and_plots_generator(self):
        generator_class = {
            'Interviewers': MetricsAndPlots,
            'Supervisors': SupervisorMetricsAndPlots,
            'Headquarters': HeadquatersMetricsAndPlots,
        }[self.current_user_group]
        return generator_class(user_login=self.current_user.login)

    def get_sections_skeleton_filled(self):
        sections_skeleton = self.get_sections_skeleton()
        generator = self.get_metrics_and_plots_generator()

        section_methods = {
            'metrics': [method_name for method_name in dir(generator) if method_name.startswith('get_')],
            'plots': [method_name for method_name in dir(generator) if method_name.startswith('plot_')],
        }

        position = 0
        for section in sections_skeleton:
            if section['section_type'] == 'metrics':
                for bloc in section['section_data']:
                    method = getattr(generator, section_methods['metrics'][position])
                    if 'selected_interviewer' in inspect.signature(method).parameters:
                        selected_interviewer = self.request.POST.get('interviewer', None)
                        bloc['value'] = method(selected_interviewer=selected_interviewer)
                    else:
                        bloc['value'] = method()
                    position += 1

        position = 0
        for section in sections_skeleton:
            if section['section_type'] == 'plots':
                for bloc in section['section_data']:
                    method = getattr(generator, section_methods['plots'][position])
                    bloc['plot'] = method()
                    position += 1

        return sections_skeleton

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.template_name = self.get_template_names()
        section_to_render = self.get_sections_skeleton_filled()

        if self.current_user_group == 'Supervisors':
            interviewer_choices = [
                (interviewer.login, interviewer.fullname) for interviewer in
                CustomUser.objects.filter(Q(supervisor=self.current_user.login))
            ]
            if self.request.method == 'POST':
                form = InterviewerSelectForm(self.request.POST, interviewer_choices=interviewer_choices)
                if form.is_valid():
                    selected_interviewer = form.cleaned_data['interviewer']
            else:
                form = InterviewerSelectForm(interviewer_choices=interviewer_choices)

            context['form'] = form
        context['sections'] = section_to_render

        return context

    def handle_ajax(self, request, *args, **kwargs):
        if self.current_user_group == 'Supervisors':
            selected_interviewer = request.POST.get('interviewer')
            mean_duration = self.get_metrics_and_plots_generator(
                ).get_05_interviews_duration_mean(
                selected_interviewer=selected_interviewer).split(':')
            total_duration = self.get_metrics_and_plots_generator(
                ).get_06_interviews_duration_total(
                selected_interviewer=selected_interviewer).split(':')
            return JsonResponse({
                'interviewer_selected': selected_interviewer,
                'mean_duration_minutes': mean_duration[0],
                'mean_duration_seconds': mean_duration[1],
                'total_duration_minutes': total_duration[0],
                'total_duration_seconds': total_duration[1],
            })

