from django import forms
from . import models


class CreateArticle(forms.ModelForm):   #inheriting the properties from forms.ModelForm.Django will automatically generate form fields for title, body, slug, and thumb based on the Article model’s fields.
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']
