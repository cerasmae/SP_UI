# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Word(models.Model):
	word = models.CharField(max_length = 256)
	# years = ArrayField(models.CharField(max_length=10), null = True)
	# sources = ArrayField(models.CharField(max_length = 255), null = True)
	tf_idf = models.FloatField()

	def __str__(self):
		return self.word

class Year_Used(models.Model):
	year = models.PositiveIntegerField()
	word = models.CharField(max_length = 256)

	class Meta:
		unique_together = (("year", "word"),)

class CharBigram(models.Model):
	cbigram = models.CharField(max_length = 2)
	tf_idf = models.FloatField()

	def __str__(self):
		return self.cbigram

class WordBigram(models.Model):
	wbigram = models.CharField(max_length = 256)
	tf_idf = models.FloatField()

	def __str__(self):
		return self.wbigram