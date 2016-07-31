from django import models
from django.contrib.auth import get_user_model
from django.contrib.translations import ugettext_lazy as _

from organizations.models import Organization
from projects.models import Cause, Project


User = get_user_model()


class Contributor(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Login user'))

    photo = models.ImageField(path='contributor_photos', verbose_name=_('Contributor photo'))

    supported_causes = models.ManyToManyField(Cause)

    supported_projects = models.ManyToManyField(Project)

    supported_organizations = models.ManyToManyField(Organization)

    def __repr__(self):
        return '<Contributor({!r}, active={!r})>'.format(self.user.username,
                                                         self.user.is_active)

    def __str__(self):
        return self.user.get_full_name()
