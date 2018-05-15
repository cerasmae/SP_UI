# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Words.models import Word

# Create your views here.
def index(request):
	all_words = Word.objects.all()

	return render(request, 'index.html', {"all_words":all_words})


def tables(request):
	all_words = Word.objects.all()

	return render(request, 'tables.html', {"all_words":all_words})