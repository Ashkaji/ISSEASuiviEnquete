from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.models import Supervisor, Controller, Interviewer, SubSupervisor


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
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

    def add_bloc_to_section(self, section_type, section_rank=None, bloc_rank=None, **details):
        """
        Adds a block to a section of the specified type.

        Args:
            section_type (str): The type of section. Must be one of the keys of the `sections_data` attribute.
            section_rank (int, optional): The rank of the section. If not specified, the last section is used.
                If the specified rank does not exist and cannot be created by adding a new section, a ValueError is raised.
            bloc_rank (int, optional): The rank of the block. If not specified, the block is added last.
            **details: Dictionary containing the details of the block.

        Raises:
            ValueError: If the section type is invalid or the specified section rank cannot be created.
        """
        if section_type not in self.sections_data:
            raise ValueError("The section type {} is invalid.".format(section_type))

        try:
            target_section = self.sections_data[section_type][section_rank]
        except TypeError:
            if not self.sections_data[section_type]:
                self.sections_data[section_type].append([])
            section_rank = self.number_of_sections[section_type] - 1
        except IndexError:
            if abs(section_rank) > self.number_of_sections[section_type]:
                raise ValueError("The specified section rank {} does not exist.".format(section_rank))
            if section_rank == self.number_of_sections[section_type]:
                if not self.sections_data[section_type]:
                    self.sections_data[section_type].append([])
                    section_rank = self.number_of_sections[section_type] - 1
                else:
                    self.sections_data[section_type].append([])

        if bloc_rank is None:
            bloc_rank = len(self.sections_data[section_type][section_rank])

        self.sections_data[section_type][section_rank].insert(bloc_rank, details)

    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['header_message'] = self.header_message
        context['metric_sections'] = self.sections_data['metrics']
        context['plot_sections'] = self.sections_data['plots']
        context['geographic_sections'] = self.sections_data['geographic']

        return context
