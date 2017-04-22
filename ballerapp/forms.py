from django import forms
from django.contrib.auth.models import User
from ballerapp.models import UserProfile, Adresse




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class AddNewPlace(forms.ModelForm):
    
    class Meta:

        model = Adresse
        fields = ('country', 'city', 'street', 'hous_number', 'place_pic',)