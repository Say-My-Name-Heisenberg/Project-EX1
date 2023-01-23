from django import forms

class RegForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    experience =forms.IntegerField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)

    def clean(self):
        cleaned_data=super().clean()
        exp=req.POST.get("experience")
        if exp <= 0:
            msg="Experience can't be null"
            self.add_error("experience",msg)
       

class LogForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)

    