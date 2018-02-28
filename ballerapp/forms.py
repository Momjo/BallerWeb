from django import forms
from django.contrib.auth.models import User
from ballerapp.models import Adresse  # UserProfile,
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username...'}))
    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password...'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('website', 'picture')


class AddNewPlace(forms.ModelForm):
    country = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'country...'}))
    city = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city...'}))
    street= forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'street...'}))
    hous_number = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'number...'}))
    place_pic = forms.FileField(required=True,)

    class Meta:
        model = Adresse
        fields = ('country', 'city', 'street','hous_number', 'place_pic')



class UserLoginForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password...'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)
