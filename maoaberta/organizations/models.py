from django.db import models


class Necessity(models.Model):
    """
    Item or service that an organization regularly needs
    """
    name = models.CharField(max_length=20)
    satisfied = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)
