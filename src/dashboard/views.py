from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.models import Supervisor, Controller, Interviewer, SubSupervisor


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    """
    section_type: keys of the section_metadata property, 'metrics', 'plots' or 'geographic'
    """
    template_name = 'dashboard/base-dash.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sections_data = {'metrics': [], 'plots': [], 'geographic': [], }

    @property
    def current_user(self):
        return self.request.user

    @property
    def current_user_type(self):
        return type(self.current_user)

    @property
    def number_of_sections(self):
        """
        Returns a dictionary containing the number of sections for each type.
        """
        return {
            'metrics': len(self.sections_data['metrics']),
            'plots': len(self.sections_data['plots']),
            'geographic': len(self.sections_data['geographic']),
        }

    @property
    def header_message(self, *args, **kwargs):
        principal_message = """<h1>Bienvenu sur votre tableau de bord!</h1>
        <p>Vous trouverez toutes les informations dont 
        vous avez besoin pour une meilleure collecte"""
        personalised_msg = {
            Supervisor: ' dans votre zone</p>',
            Interviewer: '</p>',
            Controller: ' de vos enquêteurs</p>',
            SubSupervisor: ' pour vos controleurs</p>',
        }
        _header_msg = 'Nothing to show'
        if isinstance(self.current_user, (Supervisor, SubSupervisor, Controller, Interviewer)):
            _header_msg = principal_message + personalised_msg.get(self.current_user_type)

        return _header_msg

    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['header_message'] = self.header_message
        context['metric_sections'] = self.sections_data['metrics']
        context['plot_sections'] = self.sections_data['plots']
        context['geographic_sections'] = self.sections_data['geographic']

        return context
