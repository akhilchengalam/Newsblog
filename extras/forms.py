from django import forms
from .models import Subscribers



class SubscribersForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Subscribers
        fields = ('email', )

class ContactForm(forms.Form):
    name = forms.CharField(max_length=35, required=True, help_text='Give youer name')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    mobile = forms.CharField(max_length=10, help_text='Your Mobile number')
    message = forms.CharField(max_length=500, required=True,help_text='Required. Provide a subject here')
