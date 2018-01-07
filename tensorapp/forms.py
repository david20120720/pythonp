# -*- coding: utf-8 -*-

from django.forms import ModelForm
from tensorapp.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title','contents','url','email']
