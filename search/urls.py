from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^curate/$', views.curate, name='curate'),
    url(r'^arxiv_xml/$', views.arxiv_xml, name='arxiv_xml'),
    url(r'^curate_arxiv_article/$', views.curate_arxiv_article, name='curate_arxiv_article'),
]
