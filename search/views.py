# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



from .models import *
from .forms import ArticleForm

# Create your views here.

def index(request):
    template = loader.get_template('search/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def arxiv_xml(request):
    arxiv = ArxivXML.objects.filter(curated="0")[0:1].get()
    response_data = {}
    response_data['id'] = arxiv.id
    response_data['title'] = arxiv.title
    response_data['authors'] = arxiv.authors
    response_data['abstract'] = arxiv.abstract
    response_data['arxiv_id'] = arxiv.arxiv_id
    return JsonResponse(response_data)

def curate(request):
    template = loader.get_template('search/curate.html')
    form = ArticleForm()
    context = {'form': form}
    return HttpResponse(template.render(context, request))


def curate_arxiv_article(request):
    return JsonResponse("hello")
