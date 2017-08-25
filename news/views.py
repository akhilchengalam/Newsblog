from _ast import operator
from functools import reduce
from pydoc import pager

import builtins
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
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

    """Display the category wise news list"""

    model = NewsCatagories
    template_name = 'news/news_list.html'
    context_object_name = 'category'

    def get_queryset(self):
        pk = self.kwargs.get('pk','lat')
        if pk != 'lat' :
            q = self.model._default_manager.get(pk=int(pk))
            return q.news_set.all()
        else :
            return self.model._default_manager.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk',1)
        context['pgcat'] = self.model.objects.get(pk=int(pk))
        return context


class DetailView(generic.DetailView):

    """Dispaly the news in detail"""

    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'


class Searchview(generic.ListView):

    """Dispaly the search results"""

    model = News
    template_name = 'news/search_results.html'
    context_object_name = 'search_news'
    paginate_by = 7

    def get_queryset(self, *args, **kwargs):
        return News.objects.filter(title__icontains=self.request.GET['key'])

    def get_context_data(self):

        # Call the base implementation first to get a context
        context = super().get_context_data()
        category_list = NewsCatagories.objects.all()
        context['category_list'] = category_list
        return context
