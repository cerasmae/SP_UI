# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Words(models.Model):
	word = models.CharField(max_length = 255)
	# years = ArrayField(models.CharField(max_length=10), null = True)
	# sources = ArrayField(models.CharField(max_length = 255), null = True)
	tf_idf = models.FloatField()

	def __str__(self):
		return self.word