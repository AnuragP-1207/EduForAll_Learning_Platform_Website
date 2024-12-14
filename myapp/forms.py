# forms.py
from django import forms
from .models import CommunityMessage

class CommunityMessageForm(forms.ModelForm):
    class Meta:
        model = CommunityMessage
        fields = ['message']
