from django.views.generic import TemplateView


class ContributorView(TemplateView):

    template_name = 'contributors/contributor_details.html'
