from django.conf.urls import url
from extras import views


app_name = 'extras'
urlpatterns = [

    url(r'^newsletter/$', views.SubscriberView.as_view(), name='subscribe'),
    url(r'^activatesubscription/(?P<token>[0-9A-Za-z]{32})',
        views.ActivateSubscription.as_view(), name='activate_subscription'),
    url(r'^comment/(?P<pk>[-\d]+)', views.CommentsView.as_view(), name='refresh_post'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),

]
