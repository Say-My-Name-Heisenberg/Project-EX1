from django import forms

class RegForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    experience =forms.IntegerField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)
    # def clean(self):
    #     cleaned_data=super().clean()
    #     exp=cleaned_data.get("experience")
    #     if exp < 1:
    #         msg="Experience can't be null"
    #         self.add_error("experience",msg)
    def clean(self):
        cleaned_data =super().clean()
        fname=cleaned_data.get("first_name")
        lname=cleaned_data.get("last_name")
        exp=cleaned_data.get("experience")

        if fname == lname:
            msg = "first name and last name cant be same"
            self.add_error("first_name",msg)
            self.add_error("last_name",msg)

        if exp <= 0:
            msg="Experience can't be null"
            self.add_error("experience",msg)


class LogForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)

    