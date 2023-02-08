from django import forms
from .models import Staff

class RegForm(forms.Form):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter first Name","class":"form-control"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter Last Name","class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter Your G-mail","class":"form-control"}))
    experience =forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter Number of years","class":"form-control"}))
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"Enter Username","class":"form-control"}))
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control"}))
    

    # def clean(self):
    #     cleaned_data =super().clean()
    #     fname=cleaned_data.get("first_name")
    #     lname=cleaned_data.get("last_name")
    #     exp=cleaned_data.get("experience")

    #     if fname == lname:
    #         msg = "first name and last name cant be same"
    #         self.add_error("first_name",msg)
    #         self.add_error("last_name",msg)

    #     if exp <= 0:
    #         msg="Experience can't be null"
    #         self.add_error("experience",msg)


class LogForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"Enter Username","class":"form-control"}))
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control"}))
   

class RegModelForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields="__all__"
        widgets={
            "first":forms.TextInput(attrs={"class":"form-control"}),
            "last":forms.TextInput(attrs={"class":"form-control"}),
            "mail":forms.EmailInput(attrs={"class":"form-control"}),
            "exp":forms.NumberInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }

    def clean(self):
        cleaned_data =super().clean()
        fname=cleaned_data.get("first")
        lname=cleaned_data.get("last")
        exp=cleaned_data.get("exp")

        if fname == lname:
            msg = "first name and last name cant be same"
            self.add_error("first",msg)
            self.add_error("last",msg)

        if exp <= 0:
            msg="Experience can't be null"
            self.add_error("exp",msg)
   

class StaffForm(forms.Form):
    details =forms.TimeField()
    