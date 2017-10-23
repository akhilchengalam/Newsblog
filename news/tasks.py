import string
from email.message import EmailMessage
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.core.mail import EmailMessage

from django.template.loader import render_to_string
from news.models import News


@periodic_task(run_every=crontab(minute='*/1'))
def send_mail_periodically():
   print("hi")
   obj = News.objects.filter(published=True,subscribed=False)
   if obj:
       obj.update(subscribed=True)
       # obj = News.objects.last()
       html_content = render_to_string('extras/subscription_mail.html', {'news': obj})
       print(html_content)
       message = EmailMessage(subject='Newsletter', body=html_content,
                                      to=list(Subscribers.objects.filter(is_active=True).distinct()))
       message.content_subtype = 'html'
       # message.send()
       print("hi2")