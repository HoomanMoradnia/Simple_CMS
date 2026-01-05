from django.shortcuts import render
from .models import Article
from django.template import loader
from django.http import HttpResponse


def main_page(request):
    articles = Article.published.all()
    return render(request, 'blogs/list.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.published.get(slug=slug)
    return render(request, 'blogs/post.html', {'article': article})