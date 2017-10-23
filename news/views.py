from _ast import operator
from functools import reduce
from pydoc import pager

import builtins
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render
from django.dispatch import receiver
from django.views import generic
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.db.models.signals import post_save
from django.template import loader, Context
from django.core.mail import send_mail
from extras.models import Subscribers
from faker import Factory


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
    paginate_by = 10

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



@receiver(post_save, dispatch_uid="updated_news", sender=News)
def my_handler(sender, instance,  **kwargs):

    html_template = loader.get_template('extras/subscription_mail.html')
    template = loader.get_template('extras/subscription_text.html')
    context = { 'news': instance }
    html_message  = html_template.render(context)
    message = template.render(context)
    # news = News.objects.filter(title=instance.title)
    if instance.published == True:
        send_mail(
            'ReportersNews - New News Published - %s'%instance.title,
            message,
            'subscription@thereportersnews.com',
            list_of_subscribers(),
            fail_silently=False,
            html_message=html_message,
            )
    instance.subscribed=True
    return HttpResponse()

post_save.connect(my_handler, sender=News)

def list_of_subscribers():
    ls = Subscribers.objects.all()
    return [n for n in ls]


def rand(request):
    r = Factory.create()
    num = 1
    num = request.GET['id']
    n=90
    while(n>0):
        q = News()
        q.title = "%s"%(r.text()[:20])
        q.catagory = NewsCatagories.objects.get(id=num)
        q.body = r.text()
        q.save()
        n-=1
    return HttpResponse("Done ! ")


