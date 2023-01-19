from django import forms

class OpForm (forms.Form):
    n1 = forms.IntegerField(label="Enter first Number")
    n2 = forms.IntegerField(label="Enter Second Number")