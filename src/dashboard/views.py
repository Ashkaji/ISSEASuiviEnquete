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
    def number_of_metric_sections(self):
        return len(self.sections_data['metrics'])

    @property
    def number_of_plot_sections(self):
        return len(self.sections_data['plots'])

    @property
    def number_of_geographic_sections(self):
        return len(self.sections_data['geographic'])

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

    def add_section(self, section_type, rank=None):
        """
        Adds a new section to the specified section type in the sections_data dictionary.

        Args:
            section_type (str): The key in the sections_data dictionary representing the type of section (e.g., 'metrics', 'plots', 'geographic').
            rank (int, optional): The desired rank (position) for the new section within the section type. Defaults to None (appended at the end).

        Returns:
            int: The rank (position) of the newly added section.
        """
        if section_type not in self.sections_data:
            raise ValueError(f"Invalid section type: {section_type}")

        new_section = []
        if rank is None:
            self.sections_data[section_type].append(new_section)
            return len(self.sections_data[section_type]) - 1  # Return the rank of the newly added section
        else:
            if 0 <= rank <= len(self.sections_data[section_type]):
                self.sections_data[section_type].insert(rank, new_section)
                return rank
            else:
                raise IndexError(
                    f"Invalid rank {rank} for section type '{section_type}'. Rank must be between 0 and {len(self.sections_data[section_type])}")

    def add_bloc_to_section(self, section_type, section_rank=None, bloc_rank=None, **details):
        """
        Adds a new bloc (data block) to the specified section within the sections_data dictionary.

        Args:
            section_type (str): The key in the sections_data dictionary representing the type of section (e.g., 'metrics', 'plots', 'geographic').
            section_rank (int, optional): The rank (position) of the section within the section type to add the bloc to. Defaults to None (uses the last section).
            bloc_rank (int, optional): The desired rank (position) for the new bloc within the section. Defaults to None (appended at the end).
            **details (dict): Key-value pairs representing the details (data) of the bloc.

        Returns:
            int: The rank (position) of the newly added bloc within the section.
        """

        if section_type not in self.sections_data:
            raise ValueError(f"Invalid section type: {section_type}")

        if not self.sections_data[section_type]:
            self.add_section(section_type)

        if section_rank is None:
            section_rank = len(self.sections_data[section_type]) - 1  # Use the last section by default

        if 0 <= section_rank < len(self.sections_data[section_type]):
            if bloc_rank is None:
                self.sections_data[section_type][section_rank].append(details)
                return len(self.sections_data[section_type][section_rank]) - 1  # Return the rank of the newly added bloc
            else:
                if 0 <= bloc_rank <= len(self.sections_data[section_type][section_rank]):
                    self.sections_data[section_type][section_rank].insert(bloc_rank, details)
                    return bloc_rank
                else:
                    raise IndexError(
                        f"Invalid rank {bloc_rank} for section type '{section_type}' (section rank {section_rank}). Rank must be between 0 and {len(self.sections_data[section_type][section_rank])}")
        else:
            raise IndexError(
                f"Invalid section rank {section_rank} for section type '{section_type}'. Rank must be between 0 and {len(self.sections_data[section_type])}")

    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.add_bloc_to_section(section_type='metrics', section_rank=0, bloc_rank=0, title='Charge de travail', icon='', value='10', unit='Ménage(s)')
        self.add_bloc_to_section(section_type='metrics', section_rank=0, bloc_rank=1, title='Charge de travail', icon='', value='10', unit='Ménage(s)')
        self.add_bloc_to_section(section_type='metrics', section_rank=1, bloc_rank=0, title='Charge de travail', icon='', value='10', unit='Ménage(s)')
        self.add_bloc_to_section(section_type='metrics', section_rank=1, bloc_rank=1, title='Charge de travail', icon='', value='10', unit='Ménage(s)')

        context['header_message'] = self.header_message
        context['metric_sections'] = self.sections_data['metrics']
        context['plot_sections'] = self.sections_data['plots']
        context['geographic_sections'] = self.sections_data['geographic']

        return context
