# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=50, verbose_name='Наименование')
    article_description = models.CharField(max_length=500, verbose_name='Описание')
    article_title_img = models.CharField(max_length=50)
    article_text = models.TextField()
    article_date = models.DateTimeField()

    class Meta:
        ordering = ['-article_date']


class Comments(models.Model):
    comments_name = models.CharField(max_length=50, default='Аноним', verbose_name='Ваше имя')
    comments_text = models.TextField(verbose_name='Ваш комментарий')
    comments_article = models.ForeignKey(Article)
