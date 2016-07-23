from django.db import models
from django.utils.translation import ugettext_lazy as _

from contributors.models import Contributor
from projects.models import Project


class Necessity(models.Model):
    """
    Item or service that an organization regularly needs
    """
    name = models.CharField(verbose_name=_('Name'), max_length=20)
    satisfied = models.BooleanField(verbose_name=_('Satisfied'), default=False)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(
        max_length=64, verbose_name=_('Name'), help_text=_('Organization name')
    )

    description = models.TextField(
        verbose_name=_('Description'), help_text=_('Organization description')
    )

    photo = models.ImageField(verbose_name=_('Photo'), path='organization_photos')

    coordinator = models.ForeignKey(
        Contributor, verbose_name=_('Coordinator'),
        help_text=_('Person responsible for the organization')
    )

    projects = models.ManyToManyField(Project)

    necessities = models.ManyToManyField(Necessity)

    necessity_description = models.TextField(
        verbose_name=_('Necessity description'),
        help_text=_('Text to explain the organization material needs')
    )

    email = models.EmailField(
        verbose_name=_('Organization email'), blank=True,
        help_text=_('Contact email for the organization')
    )

    homepage_url = models.URLField(
        verbose_name=_('Homepage URL'), blank=True,
        help_text=_('Organization homepage link'),
    )

    facebook_url = models.URLField(
        verbose_name=_('Facebook URL'), blank=True,
        help_text=_('Organization facebook link')
    )

    twitter_url = models.URLField(
        verbose_name=_('Twitter URL'), blank=True,
        help_text=_('Organization twitter link')
    )

    def __repr__(self):
        return '<Organization({})>'.format(self.name)

    def __str__(self):
        return self.name
