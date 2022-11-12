from django import forms
from django.forms import widgets


class GuestBookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label="Имя")
    email = forms.EmailField(max_length=50, required=True, label="Email")
    text = forms.CharField(max_length=500, required=True, label="Текст",
                           widget=widgets.Textarea(attrs={'cols': 40, 'rows': 3}))