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
from .forms import ArticleForm, UploadArxivXMLForm
from .file_upload import handle_uploaded_arxiv_xml

import xml.etree.ElementTree as ET


# Create your views here.

def index(request):
    template = loader.get_template('search/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def arxiv_xml(request):
    user_id = request.user.id
    arxiv = ArxivXML.objects.filter(curated="0").filter(user_id=user_id)[0:1].get()

    response_data = {}
    response_data['id'] = arxiv.id
    response_data['title'] = arxiv.title
    response_data['authors'] = arxiv.authors
    response_data['abstract'] = arxiv.abstract
    response_data['arxiv_id'] = arxiv.arxiv_id
    response_data['user_name'] = request.user.username

    request.session["arxiv_xml_id"] = arxiv.id
    return JsonResponse(response_data)

@login_required
def curate(request):
    template = loader.get_template('search/curate.html')
    form = ArticleForm()
    context = {'form': form}
    return HttpResponse(template.render(context, request))

# At some point need to finalize validations and making this workflow a little more professional
@login_required
def curate_arxiv_article(request):
    user_id = request.user.id
    form = ArticleForm(request.POST)

    if form.is_valid():
        arxiv_xml_inst = get_object_or_404(ArxivXML, pk= request.session.get('arxiv_xml_id', False))

        article_inst = Article(trap= form.cleaned_data['trap'],
                                spin_imbalance = form.cleaned_data['spin_imbalance'],
                                mass_imbalance = form.cleaned_data['mass_imbalance'],
                                gs_ft          = form.cleaned_data['gs_ft'],
                                dimension      = form.cleaned_data['dimension'],
                                particles      = form.cleaned_data['particles'],
                                title          = arxiv_xml_inst.title,
                                link           = "https://arxiv.org/abs/" + arxiv_xml_inst.arxiv_id.replace("oai:arXiv.org:", ""),
                                authors        = arxiv_xml_inst.authors,
                                )

        arxiv_xml_inst.curated = True
        arxiv_xml_inst.save()
    return redirect('curate')

@login_required
def upload_arxiv_xml(request):
    template = loader.get_template('search/arxiv_xml_upload.html')
    form = UploadArxivXMLForm()
    context = {'form': form}

    return HttpResponse(template.render(context, request))

@login_required
def handle_arxiv_xml_upload(request):
    user_id = request.user.id
    form = UploadArxivXMLForm(request.POST, request.FILES)

    if form.is_valid():
        handle_uploaded_arxiv_xml(request.FILES['file'], user_id)

    return redirect('upload_arxiv_xml')
