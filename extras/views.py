from django.shortcuts import render
from .models import *
from django.views.generic import FormView
from django.utils.crypto import get_random_string
from .forms import SubscribersForm, ContactForm
from django.views import View
from django.http import HttpResponse, Http404
from django.core.mail import send_mail, mail_managers
from django.shortcuts import render, redirect
from django.views import generic
from news.models import News
from django.template import Context
from django.template.loader import get_template


class SubscriberView(FormView):
    model_form = SubscribersForm
    model = Subscribers
    template_name = "extras/subscriber_status.html"
    fields = ['email',]
    success_url = '/'

    def form_invalid(self,form):
        return render(self.request, {'form':self.model_form(form),'msg':msg,})

    def post(self, request, *args, **kwargs):
        form = self.model_form(request.POST)
        if form.is_valid():
            print('form valid')
            email = form['email'].value()

            msg=" ";
            email_exist = Subscribers.objects.filter(email=email)
            # print("%s"%(email_in_db))
            if email_exist:
                 msg = 'You Are Already Subscribed To our NewsLetter.'
                 msg = "<div class='alert alert-info'><b>STATUS :</b> %s</div>"%(msg)
            else:
                m = Subscribers()
                m.email = email
                m.token = get_random_string(length=32)
                m.active=False
                m.save()
                send_mail(
                    'Subscription Activation Approval',
                    """ Hey User, This email ( %s ) have been requested to subscribe in our News Channel, \
                    if You are Interested Please Activate through this link :  \
                    \
                        http://127.0.0.1:8000/extras/activatesubscription/%s/    \
                    \


                    From The Reporters News.com
                    """%(m.email, m.token),
                    'activate-subscription@reportersnews.com',
                    [m.email],
                    fail_silently=True,
                    )
                msg = 'Successfully Subscribed! Activate It From Your Inbox.'
                msg = "<div class='alert alert-success'><b>STATUS :</b> %s</div>"%(msg)
            print(msg)

        else:
            print('form_invalid')
            msg="Invalid Email"
            msg = "<div class='alert alert-danger'><b>STATUS :</b> %s</div>"%(msg)
        return HttpResponse(msg)


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.model_form()})


class ActivateSubscription(View):
    """docstring for ActivateSubscription."""

    def get(self, request, *args, **kwargs):
        """uidb64, token"""
        try:
            token = self.kwargs['token']
            subscriber = Subscribers.objects.get(token=token)
            subscriber.backend='django.contrib.auth.backends.ModelBackend'

        except (TypeError, ValueError, OverflowError, Subscribers.DoesNotExist):
            subscriber = None

        if subscriber is not None :
            subscriber.is_active = True
            subscriber.save()
            return redirect('news:home')
        else:
            return render(request, 'extras/subscription_activation_invalid.html')


class CommentsView(generic.DetailView):
    # template_name = 'comments/loadcomment.html'
    model = News
    context_object_name = 'news'


class ContactView(generic.TemplateView):
    template_name = 'extras/contactus.html'
    model_form = ContactForm


    def post(self, request, *args, **kwargs):
        form = self.model_form(request.POST)
        if form.is_valid:
            print('form valid')
            name = form['name'].value()
            email = form['email'].value()
            mobile = form['mobile'].value()
            message = form['message'].value()

            content = "%s %s %s %s " % (name,email,mobile,message)

            mail_managers('New Contact form submission',content,
                fail_silently=False)


        else:
            form = ContactForm()

        return render(request, 'extras/contactus.html', {'form': form})
