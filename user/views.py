from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from .models import Profile,User
import user
from .forms import *
from .tokens import account_activation_token
from django.views import View
from django.conf import settings



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            # to_email = form.cleaned_data.get('email')
            # from_email = 'thereportersnews@gmail.com'
            # email = EmailMessage(mail_subject, message, from_email = from_email, to=[to_email] )
            # email.send()
            # template_name = 'registration/account_activation_email_sent.html'
            # return render(request, template_name)

            user.email_user(mail_subject, message)
            # return redirect('registration/account_activation_email_sent')
            template_name = 'registration/account_activation_email_sent.html'
            return render(request, template_name)


    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


#Account Activation

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:

        return render(request, 'registration/account_activation_invalid.html')



class Updatepasswordview(FormView):
    template_name = 'user/update_password.html'
    form_class = Passwordchangeform
    success_url = '/'

    def form_valid(self, form):
        pas = super(Updatepasswordview ,self).form_valid(form)
        form = form.cleaned_data
        if(form['password'] == form['password_confirm']):
            self.request.user.set_password(form['password'])
            self.request.user.save()
            update_session_auth_hash(self.request, self.request.user)  # Important!
            login(self.request, self.request.user)

        return pas


class Updateprofileview(FormView):
    template_name = 'user/update_profile.html'
    form_class = Profileupdateform
    success_url = '/'

    def form_valid(self,form):
        form = form.cleaned_data
        pro = super(Updateprofileview, self).form_valid(form)
        if(pro):
            self.request.user.first_name = form['first_name']
            self.request.user.last_name = form['last_name']
            self.request.user.email = form['email']
            self.request.user.save()
        return pro
