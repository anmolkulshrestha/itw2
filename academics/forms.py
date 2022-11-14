from django import forms
from .models import Message
class ContactUsForm(forms.ModelForm):
    class Meta :
        fields = ['message']
        model = Message