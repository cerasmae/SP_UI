"""SP_UI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^least_used$', views.least_used, name='least_used'),
    url(r'^character_bigrams$', views.char_bigrams, name='char_bigram'),
    url(r'^unigram/(?P<word>[0-9A-Za-z._%+-]+)', views.comparisons, name='comparisons'),
    url(r'^word_bigrams$', views.word_bigrams, name='word_bigram'),
    url(r'^char_bigrams/(?P<word>[0-9A-Za-z._%+-]+)', views.cb_comparisons, name='cb_comparisons'),
    url(r'^word_bigrams/(?P<word>[0-9A-Za-z._%+-]+( [a-zA-Z0-9_]+))', views.wb_comparisons, name='wb_comparisons'),
    url(r'^unique_words/(?P<starts>[0-9A-Za-z._%+-]+)', views.sectioning, name='sectioning'),
    url(r'^unique_word_bigrams/(?P<starts>[0-9A-Za-z._%+-]+)', views.sectioning_wb, name='sectioning_wb'),
]
