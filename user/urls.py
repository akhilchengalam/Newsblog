from django.conf.urls import url
from Report.settings import DEBUG as DEVELOPMENT_MODE
from news import views
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'user'
urlpatterns = [

#urls for login/logout
    url(r'^login/$', auth_views.login,{'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'news/index.html', 'next_page': '/'}, name='logout'),
    url(r'^registration/$',SignupView.as_view(),  name='signup'),

]