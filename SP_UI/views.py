# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Words.models import Word, CharBigram

# Create your views here.
def index(request):
	top_100 = Word.objects.all().order_by("tf_idf")

	top_100 = top_100[:100]

	return render(request, 'index.html', {"top_100": top_100, "title": "Most Used Words"})
	# return render(request, 'index.html')

def least_used(request):
	least_used = Word.objects.all().order_by("-tf_idf")

	least_used = least_used[:100]

	return render(request, 'index.html', {"top_100": least_used, "title": "Least Used Words"})
	# return render(request, 'index.html')


def tables(request):
	all_words = Word.objects.all()

	return render(request, 'tables.html', {"all_words":all_words})

def char_bigrams(request):
	cbigrams = CharBigram.objects.filter(cbigram__iregex='^[a-z][a-z]').order_by("-tf_idf")

	return render(request, 'index.html', {"top_100": cbigrams, "title": "Character Bigrams"})

def char_map(ch):
	if ch == 'k':
		return ['c']
	if ch == 'c':
		return ['k']
	if ch == 'o':
		return ['u']
	if ch == 'u':
		return ['o', 'w']	
	return '$'

def comparisons(request, word):
	next_ch = word
	prev_chs = []
	possibilities = []
	comparisons = []
	

	for ch in word:
		next_ch = word[1:]
		chars = char_map(ch)
		possibilities = []

		for cc in chars:
			flag = False
			if len(prev_chs) > 0:
				for pc in prev_chs:
					if cc == "$":
						flag = True
						possibilities.append(pc+ch)
					else:
						possibilities.append(pc+cc)

					if not flag:
						possibilities.append(pc+ch)
			else:
				if cc == "$":
					possibilities.append(ch)
				else:
					possibilities.append(cc)

		prev_chs = possibilities[:]


	for prevs in prev_chs:
		if prevs != word:
			comp = Word.objects.filter(word=prevs).first()
			if comp:
				comparisons.append(comp)

	comparisons.append(Word.objects.filter(word=word).first())

	return render(request, 'index.html', {"top_100": comparisons, "word": word})