from django.views.generic import DetailView, TemplateView
from .models import Contributor


class LoginView(TemplateView):

    template_name = 'contributors/login.html'


class ContributorDetailView(DetailView):

    template_name = 'contributors/contributor_details.html'
    model = Contributor
