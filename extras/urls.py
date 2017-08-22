from django.conf.urls import url
from extras import views


app_name = 'extras'
urlpatterns = [

    url(r'^newsletter/$', views.SubscriberView.as_view(), name='newsletter'),


]
