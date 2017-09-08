# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# need archive and pre archiv identification... every record has a unique identifier within arxiv, we can set up a parallel system for pre arxiv and non-arxiv

# Create your models here.

# This model is what is generated by importing Arxiv data from an XML format. The 'Curated' value determines whether or not the article represented is also searchable from the main app.

class ArxivXML(models.Model):
    title = models.CharField(max_length=1000)
    authors = models.CharField(max_length=1000)
    abstract = models.TextField()
    arxiv_id = models.CharField(max_length=200)
    curated = models.BooleanField(default=False)

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
