# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    BOSON = 'bs'
    FERMION = 'fr'
    GS      = 'gs'
    FT      = 'ft'
    PARTICLE_CHOICES = (
        (BOSON, 'Bosons'),
        (FERMION, 'Fermions'),
    )
    GS_FT_CHOICES = (
        (GS, 'GS'),
        (FT, 'FT'),
    )
    dimension = models.IntegerField(default=1)
    particles = models.CharField(
        max_length=2,
        choices=PARTICLE_CHOICES,
    )
    gs_ft = models.CharField(
        max_length=2,
        choices=GS_FT_CHOICES,
    )
    trap = models.BooleanField()
    spin_imbalance = models.BooleanField()
    mass_imbalance = models.BooleanField()

    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default="none")
    def __str__(self):
        return self.title
