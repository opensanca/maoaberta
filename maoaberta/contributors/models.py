from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from organizations.models import Organization
from projects.models import Project


class Contributor(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Login user'))

    photo = models.ImageField(
        upload_to='contributor_photos', verbose_name=_('Contributor photo')
    )

    supported_projects = models.ManyToManyField(Project)

    supported_organizations = models.ManyToManyField(Organization)

    def __repr__(self):
        return '<Contributor({!r}, active={!r})>'.format(self.user.username,
                                                         self.user.is_active)

    def __str__(self):
        return self.user.get_full_name()
