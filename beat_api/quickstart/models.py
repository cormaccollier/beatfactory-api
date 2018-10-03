# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    def __unicode__(self):
        return 'Beat: ' + self.name

    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    artist = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
