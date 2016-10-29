"""maoaberta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from allauth.account.views import LoginView
from contributors.views import ContributorView, logout_view
from organizations.views import HomePageView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^contributor/$', ContributorView.as_view(), name='contributor'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^signout/$', LoginView.as_view(), name='account_signup'),
    url(r'^logout/$', logout_view, name='logout'),
]
