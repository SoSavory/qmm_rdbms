# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Article
from .models import ArxivXML

# Register your models here.
admin.site.register(Article)
admin.site.register(ArxivXML)
