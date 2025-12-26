from django.shortcuts import render
from .models import Post
from django.template import loader
from django.http import HttpResponse


def main_page(request):
    template = loader.get_template('main_page.html')
    return HttpResponse(template.render())
