from django.db import models
from django.utils.translation import ugettext_lazy as _


class Necessity(models.Model):
    """
    Item or service that an organization regularly needs
    """
    name = models.CharField(verbose_name=_('Name'), max_length=20)
    satisfied = models.BooleanField(verbose_name=_('Satisfied'), default=False)

    def __str__(self):
        return self.name
