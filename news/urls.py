from django.conf.urls import url
from news import views


app_name = 'news'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^cat/(?P<slug>[-\w]+)/', views.NewsView.as_view(), name='news_catag_list'),
    url(r'^newscatagory/(?P<pk>[0-9]+)/$', views.NewsView.as_view(), name='category'),
    url(r'^newsdetails/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^search', views.Searchview.as_view(), name='search'),

]