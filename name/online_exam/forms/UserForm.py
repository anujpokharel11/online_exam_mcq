from django import forms
from signup_login.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username', 'email']
         
       
