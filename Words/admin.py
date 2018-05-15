# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Word, CharBigram, WordBigram

class WordAdmin(admin.ModelAdmin):
    search_fields = ['word']

admin.site.register(Word, WordAdmin)
admin.site.register(CharBigram)
admin.site.register(WordBigram)