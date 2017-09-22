from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),

    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.article, name='article'),

    url(r'^uncurated_articles/$', views.uncurated_articles, name='uncurated_articles'),
    url(r'^uncurated_article/(?P<uncurated_article_id>[0-9]+)/$', views.uncurated_article, name='uncurated_article'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^curate/$', views.curate, name='curate'),
    url(r'^arxiv_xml/$', views.arxiv_xml, name='arxiv_xml'),
    url(r'^curate_arxiv_article/$', views.curate_arxiv_article, name='curate_arxiv_article'),
    url(r'^skip_arxiv_xml_curation/$', views.skip_arxiv_xml_curation, name='skip_arxiv_xml_curation'),
    url(r'^upload_arxiv_xml/$', views.upload_arxiv_xml, name='upload_arxiv_xml'),
    url(r'^handle_arxiv_xml_upload/$', views.handle_arxiv_xml_upload, name='handle_arxiv_xml_upload'),
]
