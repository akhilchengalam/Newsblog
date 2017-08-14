from pydoc import pager

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


class HomeView(generic.ListView):
    template_name = 'news/index.html'
    model = News
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        data = News.objects.order_by('-posted')
        context['latest'] = data

        newslist = NewsCatagories.objects.order_by('-id')
        context['news_list'] = newslist

        return context


class NewsView(generic.ListView):
    template_name = 'news/news_list.html'
    model = NewsCatagories


    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        data = News.objects.order_by('-posted')
        context['catag_news'] = data

        newslist = NewsCatagories.objects.order_by('-id')
        context['news_list'] = newslist

        return context

    def get_queryset(self, id, **kwargs):
        return News.objects.filter()

