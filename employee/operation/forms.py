from django import forms

class OpForm (forms.Form):
    num1 = forms.IntegerField(label="Enter first Number")
    num2 = forms.IntegerField(label="Enter Second Number")
    def clean(self):
        cleaned_data=super().clean()
        num1=cleaned_data.get("num1")
        num2=cleaned_data.get("num2")
        if num1 < 0:
            msg="input value less than zero"
            self.add_error("num1",msg)
        if num2 < 0:
            msg="input value less than zero"
            self.add_error("num2",msg)