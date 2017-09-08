# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render, redirect, get_object_or_404
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
    response_data['user_name'] = request.user.username
    request.session["arxiv_xml_id"] = arxiv.id
    return JsonResponse(response_data)

def curate(request):
    template = loader.get_template('search/curate.html')
    form = ArticleForm()
    context = {'form': form}
    return HttpResponse(template.render(context, request))

# At some point need to finalize validations and making this workflow a little more professional
def curate_arxiv_article(request):
    user_id = request.user.id
    form = ArticleForm(request.POST)

    if form.is_valid():
        # For fields that are not fed through the form, need a custom cleaner, or figure out how to implement those into the form object
        arxiv_xml_inst = get_object_or_404(ArxivXML, pk= request.session.get('arxiv_xml_id', False))

        article_inst = Article(trap= form.cleaned_data['trap'],
                                spin_imbalance= form.cleaned_data['spin_imbalance'],
                                mass_imbalance= form.cleaned_data['mass_imbalance'],
                                gs_ft= form.cleaned_data['gs_ft'],
                                dimension= form.cleaned_data['dimension'],
                                particles= form.cleaned_data['particles'],
                                title= arxiv_xml_inst.title,
                                link= request.POST['link'],
                                authors= arxiv_xml_inst.authors,
                                )

        arxiv_xml_inst.curated = True
        arxiv_xml_inst.save()
    return redirect('curate')
