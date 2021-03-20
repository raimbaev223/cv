
from django import forms


class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    subject = forms.CharField(max_length=25)
    message = forms.CharField(widget=forms.Textarea)