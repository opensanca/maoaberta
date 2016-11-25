from django.views.generic import DetailView, TemplateView
from .models import Organization


class HomePageView(TemplateView):
    template_name = 'base.html'


class OrganizationDetailView(DetailView):

    template_name = 'organizations/organization_details.html'
    model = Organization
