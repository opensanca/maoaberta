from django.db import models


class Necessity(models.Model):
    """
    Item or service that an organization regularly needs
    """
    name = models.CharField(max_length=20)
    interval = models.FloatField()

    def __str__(self):
        return '{}'.format(self.name)
