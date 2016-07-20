from django.db import models


class Project(models.Model):
    """
    Each project is an activity and/or event organized by an organization.
    """
    name = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)
