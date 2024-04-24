# Metrics and plots generator
```python
from ISSEASuiviEnquete.settings import API_URL, API_USERNAME, API_PASSWORD
from accounts.models import CustomUser
from survey_solutions_api_client import AuthenticatedClient
from survey_solutions_api_client.api.assignments import get_api_v1_assignments
from survey_solutions_api_client.api.users import get_api_v1_users_id
from survey_solutions_api_client.models import AssignmentsListView, UserApiDetails


class MetricsAndPlots:
    def __init__(self, user_login: str):
        self.user: CustomUser = CustomUser.objects.get(login=user_login)
        self.client: AuthenticatedClient = AuthenticatedClient(
            base_url=API_URL,
            username=API_USERNAME,
            password=API_PASSWORD
        )

    @property
    async def user_details(self):
        data: UserApiDetails = await get_api_v1_users_id.asyncio(
            id=self.user.login,
            client=self.client
        )
        return data

    @property
    async def user_assigments_detailed(self):
        data: AssignmentsListView = await get_api_v1_assignments.asyncio(
            client=self.client,
            responsible=self.user.login,
        )
        return data

    @property
    async def user_assigments(self):
        data: AssignmentsListView = await self.user_assigments_detailed
        return data.assignments

    @property
    async def user_questionnaires_id(self):
        user_assignments = await self.user_assigments
        return list(item.questionnaire_id for item in user_assignments)

    async def get_01_workload(self):
        user_assignments = await self.user_assigments
        return sum(item.quantity for item in user_assignments)

    async def get_02_completed_interviews_number(self):
        # get_api_v1_interviews
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

```

# Dashboard layout
```python
secction_sample = [
    {
        'section_type': 'metrics',
        'section_data': [
            {
                'title': '',
                'icon': '',
                'value': '',
                'unit': ''
            },
        ]
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
    {
        'section_type': 'geographic',
        'section_data': [
            {
                'title': '',
                'plot': ''
            }
        ]
    }
]

import pickle

interviewer_sections = [{'section_type': 'metrics', 'section_data': [{'title': 'Charge de travail', 'icon': '', 'value': '', 'unit': 'Ménages'}, {'title': 'Enquêtés', 'icon': '', 'value': '', 'unit': 'Ménages'}, {'title': 'Pourcentage enquêtés', 'icon': '', 'value': '', 'unit': 'des ménages affectés'}, {'title': 'Pourcentage net enquêtés', 'icon': '', 'value': '', 'unit': 'des ménages valides'}]}, {'section_type': 'plots', 'section_data': [{'title': 'Nombre de ménages enquêtés par jour', 'plot': ''}, {'title': 'Cumul du nombre de ménages enquêtés par jour', 'plot': ''}]}, {'section_type': 'plots', 'section_data': [{'title': 'Statut des ménages visités', 'plot': ''}, {'title': 'Statut des ménages visités par ZD', 'plot': ''}]}, {'section_type': 'plots', 'section_data': [{'title': 'Nombre de ménages enquêtés par jour et par ZD', 'plot': ''}, {'title': 'Cumul du nombre de ménages enquêtés par jour et par ZD', 'plot': ''}]}, {'section_type': 'geographic', 'section_data': [{'title': 'Carte de la zone à couvrir', 'plot': ''}]}]
supervisor_sections = [{'section_type': 'metrics', 'section_data': [{'title': 'Charge des enquêteurs', 'icon': '', 'value': '', 'unit': 'Ménages'}, {'title': 'Total enquêté', 'icon': '', 'value': '', 'unit': 'Ménages'}, {'title': 'Pourcentage enquêté', 'icon': '', 'value': '', 'unit': 'des ménages'}, {'title': 'Pourcentage net enquêté', 'icon': '', 'value': '', 'unit': 'des ménages valides'}]}, {'section_type': 'plots', 'section_data': [{'title': 'Nombre de ménages enquêtés par jour', 'plot': ''}, {'title': 'Cumul du nombre de ménages enquêtés par jour', 'plot': ''}]}, {'section_type': 'plots', 'section_data': [{'title': 'Nombre de ménages enquêtés par jour et par ZD', 'plot': ''}, {'title': 'Cumul du nombre de ménages enquêtés par jour et par ZD', 'plot': ''}, {'title': 'Nombre de ménages enquêtés par jour et par enquêteur', 'plot': ''}, {'title': 'Cumul du nombre de ménages enquêtés par jour et par enquêteur', 'plot': ''}]}, {'section_type': 'plots', 'section_data': [{'title': 'Statut des ménages visités par ZD', 'plot': ''}, {'title': 'Statut des ménages visités par enquêteur', 'plot': ''}]}, {'section_type': 'metrics', 'section_data': [{'title': 'Durée moyenne d’administration du questionnaire', 'icon': '', 'value': '', 'unit': 'minutes'}, {'title': 'Durée totale d’administration du questionnaire    ', 'icon': '', 'value': '', 'unit': 'minutes'}, {'title': 'Ménages enquêtés sans localisation GPS', 'icon': '', 'value': '', 'unit': 'Ménages'}, {'title': 'Risk Interviewer proba.', 'icon': '', 'value': '', 'unit': ''}]}, {'section_type': 'plots', 'section_data': [{'title': "Diagramme d'activité", 'plot': ''}]}, {'section_type': 'plots', 'section_data': [{'title': 'Durée d’administration du questionnaire par enquêteurs', 'plot': ''}]}, {'section_type': 'geographic', 'section_data': [{'title': 'Carte de la zone à enquêter', 'plot': ''}]}]
headquaters_sections = [{'section_type': 'metrics', 'section_data': [{'title': 'À enquêter', 'icon': '', 'value': '', 'unit': 'Ménages'}, {'title': 'Enquêtés', 'icon': '', 'value': '', 'unit': 'Ménages'}, {'title': 'Pourcentage enquêtés', 'icon': '', 'value': '', 'unit': 'des ménages'}, {'title': 'Pourcentage net enquêtés', 'icon': '', 'value': '', 'unit': 'des ménages valides'}]}, {'section_type': 'plots', 'section_data': [{'title': 'Nombre de ménages enquêtés par jour', 'plot': ''}, {'title': 'Cumul du nombre de ménages enquêtés par jour', 'plot': ''}]}, {'section_type': 'plots', 'section_data': [{'title': 'Statut des ménages visités ', 'plot': ''}, {'title': 'Cumul du statut des ménages visités ', 'plot': ''}]}, {'section_type': 'plots', 'section_data': [{'title': 'Nombre de ménages enquêtés par jour et par contrôleur', 'plot': ''}, {'title': 'Cumul du nombre de ménages enquêtés par jour et par contrôleur', 'plot': ''}]}, {'section_type': 'plots', 'section_data': [{'title': 'Statut des ménages visités par contrôleur', 'plot': ''}]}, {'section_type': 'geographic', 'section_data': [{'title': 'Carte de la zone à enquêter', 'plot': ''}]}]

with open('./src/dashboard/rendering/interviewers.pickle', 'wb') as f:
    pickle.dump(interviewer_sections, f)

with open('./src/dashboard/rendering/supervisors', 'wb') as f:
    pickle.dump(supervisor_sections, f)

with open('./src/dashboard/rendering/headquarters.pickle', 'wb') as f:
    pickle.dump(headquaters_sections, f)
```

# Deployment
Deploying a Django app on your own server involves several key steps. Here's a high-level overview of the process:

1. **Prepare Your Application**:
   - Ensure your Django project is production-ready.
   - Collect static files with `python manage.py collectstatic`.
   - Configure your `settings.py` for production (disable DEBUG, configure database, etc.).

2. **Set Up the Server**:
   - Choose a server with the required hardware and software specifications.
   - Install the necessary software, like the web server (e.g., Nginx or Apache) and application server (e.g., Gunicorn or uWSGI).
   - Configure the web server to serve your application and handle client requests.

3. **Configure WSGI/ASGI**:
   - Django supports WSGI (synchronous) and ASGI (asynchronous) interfaces.
   - Set up an application server like Gunicorn for WSGI or Daphne/Uvicorn for ASGI.

4. **Secure Your Application**:
   - Implement SSL/TLS to encrypt data transmission.
   - Set up a firewall and other security measures to protect your server.

5. **Deploy the Application**:
   - Upload your Django project to the server.
   - Use the application server to run your Django app.
   - Restart the web server to apply the changes.

6. **Monitor and Maintain**:
   - Regularly update your server and application to patch security vulnerabilities.
   - Monitor your application for uptime and performance issues.

For a detailed guide, you can refer to the [Django documentation](^2^) or follow a tutorial like the one provided by [MDN Web Docs](^1^). These resources will give you step-by-step instructions and best practices for deploying your Django app to production. Remember to go through a deployment checklist to ensure all configurations are suitable for a production environment. Good luck with your deployment!

Source: Conversation with Bing, 4/23/2024
- (1) How to deploy Django | Django documentation | Django. https://docs.djangoproject.com/en/5.0/howto/deployment/.
- (2) Django Tutorial Part 11: Deploying Django to production. https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment.
- (3) Deploy a Django App on App Platform - DigitalOcean. https://docs.digitalocean.com/developer-center/deploy-a-django-app-on-app-platform/.
- (4) Securely Deploy a Django App With Gunicorn, Nginx, & HTTPS. https://realpython.com/django-nginx-gunicorn/.
- (5) Django Hosting & Deployment Options - LearnDjango.com. https://learndjango.com/tutorials/django-hosting-deployment-options.
- (6) Deploy a Django project - Bitnami. https://docs.bitnami.com/aws/infrastructure/django/get-started/deploy-django-project/.
- (7) null. https://bing.com/search?q=.