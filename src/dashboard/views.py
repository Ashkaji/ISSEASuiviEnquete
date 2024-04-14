from __future__ import print_function

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

from ISSEASuiviEnquete.settings import API_USERNAME, API_URL, API_PASSWORD

INTERVIEWER_SECTIONS = [
    {
        'section_type': 'metrics',
        'section_data': [
            {
                'title': 'Charge de travail',
                'icon': '',
                'value': '20',
                'unit': 'Ménages'
            },
            {
                'title': 'Enquêtés',
                'icon': '',
                'value': '10',
                'unit': 'Ménages'
            },
            {
                'title': 'Pourcentage enquêtés',
                'icon': '',
                'value': '50',
                'unit': '% des ménages affectés'
            },
            {
                'title': 'Pourcentage net enquêtés',
                'icon': '',
                'value': '75',
                'unit': '% des ménages valides'
            },
        ]
    },
    {
        'section_type': 'plots',
        'section_data': [
            {
                'title': 'Evolution du nombre de ménages enquêtés par jour',
                'plot': '',
            },
            {
                'title': 'Statut des ménages enquêtés ',
                'plot': '',
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
                'plot': '',
            }
        ]
    }
]
CONTROLLER_SECTIONS = [
    {
        'section_type': 'metrics',
        'section_data': [
            {
                'title': 'Charge des enquêteurs',
                'icon': '',
                'value': '25',
                'unit': 'Ménages'
            },
            {
                'title': 'Total enquêtés',
                'icon': '',
                'value': '',
                'unit': 'Ménages'
            },
            {
                'title': 'Pourcentage enquêtés',
                'icon': '',
                'value': '5',
                'unit': '% des ménages affectés'
            },
            {
                'title': 'Pourcentage total net enquêtés',
                'icon': '',
                'value': '15',
                'unit': '% des ménages valides'
            },
        ]
    },
    {
        'section_type': 'metrics',
        'section_data': [
            {
                'title': 'Durée moyenne d’administration du questionnaire ',
                'icon': '',
                'value': '',
                'unit': 'minutes'
            },
            {
                'title': 'Durée totale d’administration du questionnaire ',
                'icon': '',
                'value': '',
                'unit': 'minutes'
            },
            {
                'title': 'Ménages non localicés',
                'icon': '',
                'value': '',
                'unit': 'Ménages'
            },
            {
                'title': 'Interviewer à risque',
                'icon': '',
                'value': '',
                'unit': '% de chances'
            },
        ]
    },
    {
        'section_type': 'plots',
        'section_data': [
            {
                'title': 'Evolution du nombre de ménages enquêtés par jour',
                'plot': '',
            },
            {
                'title': 'Evolution du nombre de ménages enquêtés par jour, par enquêteur',
                'plot': '',
            },
            {
                'title': 'Evolution du nombre de ménages enquêtés par jour et par ZD',
                'plot': '',
            },
            {
                'title': 'Répartition des ménages enquêtés par statut et par ZD, par enquêteur',
                'plot': '',
            },
        ],
    },
    {
        'section_type': 'plots',
        'section_data': [
            {
                'title': '',
                'plot': '',
            },
        ],
    },
]
SUBSUPERVISOR_SECTIONS = [

]
SUPERVISOR_SECTIONS = [

]

configuration = swagger_client.Configuration()
configuration.username = API_USERNAME
configuration.password = API_PASSWORD
configuration.host = API_URL

# create an instance of the API class
api_instance = swagger_client.AssignmentsApi(swagger_client.ApiClient(configuration))

try:
    # List all assignments with filtering
    api_response = api_instance.api_v1_assignments_get(supervisor_id='C001')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->api_v1_assignments_get: %s\n" % e)


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
