from django.conf.urls import include, url

from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'Report.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^news/', include('news.urls')),
    url(r'^useraccount/', include('user.urls')),
    url(r'^', include('news.urls')),
    url(r'^extras/', include('extras.urls')),

]
