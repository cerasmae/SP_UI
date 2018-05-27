# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.urls import reverse
from collections import OrderedDict


from django.shortcuts import render

from Words.models import Word, CharBigram, WordBigram

# Create your views here.
def index(request):
	top_100 = Word.objects.all().order_by("tf_idf")

	top_100 = top_100[:100]

	return render(request, 'index.html', {"top_100": top_100, "title": "Most Used Words"})
	# return render(request, 'index.html')

def sectioning(request, starts):
	top_100 = Word.objects.filter(word__startswith=starts).order_by("word")

	return render(request, 'index.html', {"top_100": top_100, "title": "Range "+starts+" Unique Words"})

def sectioning_wb(request, starts):
	top_100 = WordBigram.objects.filter(wbigram__startswith=starts).order_by("wbigram")

	return render(request, 'wbigrams.html', {"top_100": top_100, "title": "Range "+starts+" Unique Word Bigram"})

def least_used(request):
	least_used = Word.objects.all().order_by("-tf_idf")

	least_used = least_used[:100]

	return render(request, 'index.html', {"top_100": least_used, "title": "Least Used Words"})
	# return render(request, 'index.html')


def char_bigrams(request):
	cbigrams = CharBigram.objects.filter(cbigram__iregex='^[a-z][a-z]').order_by("-tf_idf")

	return render(request, 'cbigrams.html', {"top_100": cbigrams, "title": "Character Bigrams"})

def word_bigrams(request):
	top_100 = WordBigram.objects.all().order_by("tf_idf")

	top_100 = top_100[:100]

	return render(request, 'wbigrams.html', {"top_100": top_100, "title": "Most Used Word Bigrams"})

def char_map(ch):
	if ch == 'k':
		return ['c', ch]
	if ch == 'c':
		return ['k', ch]
	if ch == 'o':
		return ['u', ch]
	if ch == 'u':
		return ['o', 'w', ch]
	if ch == 'i':
		return ['e', ch]
	if ch == 'e':
		return ['i', ch]
	if ch == 'l':
		return ['w', 'y', ch]
	return [ch]

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
			if len(prev_chs) > 0:
				for pc in prev_chs:
					possibilities.append(pc+cc)
			else:
				possibilities.append(cc)

		prev_chs = possibilities[:]

	prev_chs = list(OrderedDict.fromkeys(prev_chs))
	# print prev_chs

	for prevs in prev_chs:
		comp = Word.objects.filter(word=prevs).first()
		if comp:
			comparisons.append(comp)

	return render(request, 'index.html', {"top_100": comparisons, "word": word})

def cb_comparisons(request, word):
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
					flag = True
					possibilities.append(ch)
				else:
					possibilities.append(cc)

			# if not flag:
			possibilities.append(ch)

		prev_chs = possibilities[:]

	prev_chs = list(OrderedDict.fromkeys(prev_chs))

	for prevs in prev_chs:
		if prevs != word:
			comp = CharBigram.objects.filter(cbigram=prevs).first()
			if comp:
				comparisons.append(comp)

	comparisons.append(CharBigram.objects.filter(cbigram=word).first())

	return render(request, 'cbigrams.html', {"top_100": comparisons, "word": word})

def wb_comparisons(request, word):
	print "wb_comparisons", word
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
			if len(prev_chs) > 1:
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
					flag = True
					possibilities.append(ch)
				else:
					possibilities.append(cc)

			# if not flag:
				possibilities.append(ch)

		prev_chs = possibilities[:]

	prev_chs = list(OrderedDict.fromkeys(prev_chs))

	for prevs in prev_chs:
		if prevs != word:
			comp = WordBigram.objects.filter(wbigram=prevs).first()
			if comp:
				comparisons.append(comp)

	comparisons.append(WordBigram.objects.filter(wbigram=word).first())

	# return HttpResponseRedirect(reverse('word_bigram'), {"top_100": comparisons, "word": word})

	return render(request, 'wbigrams.html', {"top_100": comparisons, "word": word})