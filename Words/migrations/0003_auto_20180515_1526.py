# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Words', '0002_auto_20180426_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharBigram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbigram', models.CharField(max_length=2)),
                ('tf_idf', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WordBigram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wbigram', models.CharField(max_length=256)),
                ('tf_idf', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Year_Used',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('word', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterUniqueTogether(
            name='year_used',
            unique_together=set([('year', 'word')]),
        ),
    ]
