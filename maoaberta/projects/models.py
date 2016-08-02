from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

STATUS_CHOICES = (
    ('open', _('Open')),
    ('running', _('Running')),
    ('closed', _('Closed')),
)


class Project(models.Model):
    """
    Each project is an activity and/or event organized by an organization.
    """

    title = models.CharField(verbose_name=_('Title'), max_length=30)
    date = models.DateField(verbose_name=_('Date'))
    description = models.TextField(verbose_name=_('Description'))
    status = models.CharField(
        verbose_name=_('Status'), choices=STATUS_CHOICES, max_length=7, default='open'
    )
    responsible = models.ForeignKey(
        User, verbose_name=_('Responsible'), related_name='projects'
    )

    def __repr__(self):
        return '<Project({!r})>'.format(self.title)

    def __str__(self):
        return self.title
