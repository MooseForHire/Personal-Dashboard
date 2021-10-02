from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Inherits from UserCreationForm, add an optional email field
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = False)

    #Nested namespace for configurations
    class Meta:

        #User model will be affected
        model = User
        fields = ['username', 'email', 'password1', 'password2']