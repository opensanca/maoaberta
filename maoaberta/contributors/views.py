from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'contributors/login.html'

class ContributorView(TemplateView):
    template_name = 'contributors/contributor_details.html'
