from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('home')


class ContributorView(TemplateView):

    template_name = 'contributors/contributor_details.html'
