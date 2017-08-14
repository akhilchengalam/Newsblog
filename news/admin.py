from django.contrib import admin
from .models import *


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'catagory', 'body')

    class meta:
        model = News
        exclude = ('slug',)


admin.site.register(NewsCatagories)
admin.site.register(News, NewsAdmin)