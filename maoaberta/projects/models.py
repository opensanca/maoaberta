from django.contrib.auth.models import User
from django.db import models

STATUS = (
    ('open', 'open'),
    ('running', 'running'),
    ('closed', 'closed')
)


class Project(models.Model):
    """
    Each project is an activity and/or event organized by an organization.
    """
    title = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=7, default='open')
    responsible = models.ForeignKey(User, related_name='projects')

    def __str__(self):
        return '{}'.format(self.title)
