from django.db import models
from autoslug import AutoSlugField
from Report import settings
from datetime import datetime as dt
from django.urls import reverse


class NewsCatagories(models.Model):
    title = models.CharField(max_length=42)
    slug = AutoSlugField(populate_from='title',
                         unique_with=['title'],
                         unique=True, always_update=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail',kwargs={'pk':self.pk})


class News(models.Model):
    title = models.CharField(max_length=127)
    body = models.TextField(max_length=1024)
    slug = AutoSlugField(populate_from='title',
                         unique_with=['title'],
                         unique=True, always_update=True)
    catagory = models.ForeignKey('NewsCatagories', on_delete=models.SET(1))
    posted = models.DateTimeField(auto_now_add=dt.now(), blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail',kwargs={'pk':self.pk})
        
    class Meta:
        ordering = ["posted"]
        get_latest_by = "posted"
