from __future__ import unicode_literals # available for all languages -> need of research
from django.db import models


class Main(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
