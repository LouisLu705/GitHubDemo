from django import forms

class NameForm(forms.Form):
    course = forms.CharField(label='', max_length=100)