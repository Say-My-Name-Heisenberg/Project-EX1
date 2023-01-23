from django import forms

class OpForm (forms.Form):
    n1 = forms.IntegerField(label="Enter first Number")
    n2 = forms.IntegerField(label="Enter Second Number")
    def clean(self):
        cleaned_data=super().clean()
        n1=cleaned_data.get("num1")
        n2=cleaned_data.get("num2")
        if n1 < 0:
            msg="input value less than zero"
            self.add_error("num1",msg)
        if n2 < 0:
            msg="input value less than zero"
            self.add_error("num2",msg)