# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from article.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from article.models import Article, Comments


class ArticlesList(ListView):
    model = Article
    template_name = "articles.html"
    context_object_name = 'all_articles'
    paginate_by = 2


# Разобраться с DetailView и бля переписать как надо!!!!!!!!!!!!!!!!!!!!!!!!
def article(request, pk=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=pk)
    args['comments'] = Comments.objects.filter(comments_article=pk)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    args['return_path'] = request.META.get('HTTP_REFERER', '/')
    return render_to_response('article.html', args)


# Добавляем коммиты пользователей
def addcomment(request, pk):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # comment получил данные из формы form.save() ???? см 8 урок 33 мин
            comment.comments_article = Article.objects.get(id=pk)  # ищем нужную статью (ассоцируем коммиит с статьей)
            form.save()  # сохраняем изменения
    return redirect(request.META.get('HTTP_REFERER', '/'))

