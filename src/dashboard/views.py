from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="sex", y="total_bill",
                   color='smoker', barmode='group',)
fig.update_layout(margin={'t': 20, 'r': 10, 'b': 20, 'l': 10})

INTERVIEWER_SECTIONS = [
    {
        'section_type': 'metrics',
        'section_data': [
            {
                'title': 'Charge totale de travail',
                'icon': '',
                'value': '20',
                'unit': 'Ménages'
            },
            {
                'title': 'Nombre total de ménages déjà enquêtés',
                'icon': '',
                'value': '10',
                'unit': 'Ménages'
            },
            {
                'title': 'Pourcentage total de ménages enquêtés',
                'icon': '',
                'value': '50',
                'unit': '%'
            },
            {
                'title': 'Pourcentage total net de ménages enquêtés',
                'icon': '',
                'value': '75',
                'unit': '%'
            },
        ]
    },
    {
        'section_type': 'plots',
        'section_data': [
            {
                'title': 'Statut des ménages enquêtés ',
                'plot': '',
            },
            {
                'title': 'Evolution du nombre de ménages enquêtés par jour',
                'plot': fig.to_html(full_html=False),
            },
        ],
    },
    {
        'section_type': 'plots',
        'section_data': [
            {
                'title': 'Evolution du nombre de ménages enquêtés par jour et par ZD',
                'plot': '',
            },
            {
                'title': 'Répartition des ménages enquêtés par statut et par ZD',
                'plot': '',
            },
        ],
    },
    {
        'section_type': 'geographic',
        'section_data': [
            {
                'title': 'Carte de la zone à couvrir',
                'plot': fig.to_html(full_html=False),
            }
        ]
    }
]
CONTROLLER_SECTIONS = [
    {
        'section_type': 'metrics',
        'section_data': [
            {
                'title': 'Charge totale de travail par les enquêteurs',
                'icon': '',
                'value': '',
                'unit': ''
            },
            {
                'title': 'Nombre total de ménages déjà enquêtés par les enquêteurs',
                'icon': '',
                'value': '',
                'unit': ''
            },
            {
                'title': 'Pourcentage total de ménages enquêtés par les enquêteurs',
                'icon': '',
                'value': '',
                'unit': ''
            },
            {
                'title': 'Pourcentage total net de ménages enquêtés par les enquêteurs',
                'icon': '',
                'value': '',
                'unit': ''
            },
        ]
    },
]
SUBSUPERVISOR_SECTIONS = [

]
SUPERVISOR_SECTIONS = [

]


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sections_data = None

    @property
    def current_user(self):
        return self.request.user

    @property
    def current_user_group(self):
        user_groups = self.current_user.groups.all()
        if user_groups:
            return user_groups[0].name
        else:
            return None

    @property
    def header_message(self, *args, **kwargs):
        principal_message = """<h1>Bienvenu sur votre tableau de bord!</h1>
        <p>Vous trouverez toutes les informations dont 
        vous avez besoin pour une meilleure collecte"""
        personalised_msg = {
            'Supervisors': ' dans votre zone</p>',
            'Interviewers': '</p>',
            'Controllers': ' de vos enquêteurs</p>',
            'SubSupervisors': ' pour vos controleurs</p>',
        }
        _header_msg = 'Nothing to show'
        if self.current_user_group in personalised_msg.keys():
            _header_msg = principal_message + personalised_msg.get(self.current_user_group)

        return _header_msg

    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        personalised_template = {
            'Supervisors': 'dashboard/supervisor-dash.html',
            'Interviewers': 'dashboard/interviewer-dash.html',
            'Controllers': 'dashboard/controller-dash.html',
            'SubSupervisors': 'dashboard/supervisor-dash.html',
        }

        return personalised_template.get(self.current_user_group, 'dashboard/base-dash.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.template_name = self.get_template_names()

        personalised_sections_data = {
            'Supervisors': SUPERVISOR_SECTIONS,
            'Interviewers': INTERVIEWER_SECTIONS,
            'Controllers': CONTROLLER_SECTIONS,
            'SubSupervisors': SUBSUPERVISOR_SECTIONS,
        }

        context['header_message'] = self.header_message
        context['sections'] = personalised_sections_data.get(self.current_user_group, {})

        return context
