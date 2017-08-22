from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from Report.settings import DEBUG as DEVELOPMENT_MODE
from user import views

from django.contrib.auth import views as auth_views
from .views import *



urlpatterns = [

#urls for login/logout
    url(r'^login/$', auth_views.login,{'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{ 'next_page': '/news/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

#Account activation
    url(r'^activateaccount/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

#PASSWORD RESET
    # url(r'^password_reset/$', auth_views.password_reset,
    #     { 'template_name':'registration/password_reset_form.html',}, name='password_reset'),
    #
    # url(r'^password_reset/done/$', auth_views.password_reset_done,
    #     { 'template_name':'registration/password_reset_done.html',}, name='password_reset_done'),
    #
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm,
    #     {'template_name': 'registration/password_reset_confirm.html', },name='password_reset_confirm'),
    #
    # url(r'^reset/done/$', auth_views.password_reset_complete,
    #     {'template_name': 'registration/password_reset_complete.html'},name='password_reset_complete'),

    url('^', include('django.contrib.auth.urls')),

#Updadte password and profile
    url(r'^updatepassword/$', login_required(Updatepasswordview.as_view()), name='updatepassword'),
    url(r'^updateprofile/$', login_required(Updateprofileview.as_view()), name='profile'),
    #url(r'^profile/$', views.profile_update, name='profile'),

]
