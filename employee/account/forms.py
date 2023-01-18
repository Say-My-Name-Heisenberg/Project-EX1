from django import forms

class RegForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    experience =forms.IntegerField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)

class LogForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)