from django.shortcuts import render
from .models import *
from django.views.generic import FormView
from django.utils.crypto import get_random_string


class SubscriberView(FormView):
    model = Subscribers
    template_name = 'extras/subscriber_list.html'
    success_url = '/'

    def form_invalid(self,form):
        return render(self.request, self.template_name, {'form':self.model_form(form),'msg':self.msg,})

    def POST(self, request, *args, **kwargs):
        form = self.model_form(request.POST)
        if form.is_valid():
            email = form['email'].value()
            email_exist = Subscribers.objects.filter(email=email)

            if(email_exist):
                msg = 'You are already Subscribed'
                msg = "<div class='alert alert-info'><b>STATUS :</b> %s</div>"%(msg)
            else:
                 m = ReadersList()
                 m.email = email
                 m.token = get_random_string(length=32)
                 m.active=False
                 m.save()
                 send_mail(
                    'Newsletter Subscription Activation',
                     """ Hey ( %s ), this email have been requested to subscribe for our news channel,
                     Please activate the subscription through the below link : \
                        http://127.0.0.1:8000/newsletteractivate/%s/ \
                     \
                        If it was not you please ignore \
                     From TheReportersNews.com
                     """%(m.email, m.token),
                     'subscribe@thereportersnews.com',
                     [m.email],
                     fail_silently=True,
                     )
            print(msg)
        else:
            print('form_invalid')
            msg="Invalid Email"
            msg = "<div class='alert alert-danger'><b>STATUS :</b> %s</div>"%(msg)
            return render(request, self.template_name,
            {'form': self.model_form(),"msg":msg})
     def get(self, request, *args, **kwargs):
         return render(request, self.template_name, {'form': self.model_form()})
