from django.contrib.auth.views import login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.views.generic import FormView

from .forms import *
from .tokens import account_activation_token


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Activate Your Account'
#             message = render_to_string('account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)
#             return redirect('account_activation_sent')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


class SignupView(FormView):
    """Signup."""

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.backend='django.contrib.auth.backends.ModelBackend'
            user.save()
            subject = 'Activate Your Account'
            token = account_activation_token.make_token(user)
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': "127.0.0.1:8000",
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
                'html' : False,
            })
            html_message = message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': "127.0.0.1:8000",
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
                'html' : True,
            })
            user.email_user(subject, message, html_message=html_message)
            # print(message)
            template_name = 'registration/account_activation_email_sent.html'
            return render(request, template_name)
        else:
            return render(request, 'registration/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        return render(request, 'registration/signup.html', {'form': SignUpForm()})



#Activation

def activate(self, request, uidb64, token):
    try:
        uidb64 = self.kwargs['uidb64']
        user = User.objects.get(pk=uidb64)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')