from django.forms import ModelForm, Textarea
from django.forms.widgets import Input
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from models import Slide
from models import ContactInfo


class SlideForm(ModelForm):
    class Meta:
        model = Slide
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 30}),
        }
        fields = '__all__' #

class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        widgets = {
            'statement': Textarea(attrs={'cols': 80, 'rows': 30}),
        }
        fields = '__all__' #

