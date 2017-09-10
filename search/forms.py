from django import forms
from django.forms import ModelForm
from search.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['trap', 'spin_imbalance', 'mass_imbalance', 'dimension', 'particles', 'gs_ft']

class UploadArxivXMLForm(forms.Form):
    file = forms.FileField()
