from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .models import Profile, Gender

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'autocmplete' : 'text',
                'placeholder' : 'type login'
            }
        ),
        required = False,
        validators = [RegexValidator(r'[^0-9а-яА-яёЁ]', "remember, no russian")],
    )
    email = forms.EmailField(
         widget = forms.EmailInput(
            attrs = {
                'autocmplete' : 'email',
                'placeholder' : 'type your email'
            }
        ),
        required = False,
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : 'type password'
            }
        ),
        required = False,
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : 'repeat your password'
            }
        ),
        required = False,
    )

    def clean_password1(self):
        password = self.cleaned_data['password1']
        if password == '':
            raise forms.ValidationError('Type password!', code = 'invalid')
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Type username!', code = 'invalid')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('Type email!', code = 'invalid')
        return email
    
class Meta(UserCreationForm.Meta):
    fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length = 254,
        widget = forms.TextInput(
            attrs= {
                'autocomplete' : 'text',
                'placeholder' : 'login/username'
            }
        ),
        required= False
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs= {
                'autocomplete' : 'current-password',
                'placeholder' : 'password'
            }
        ),
        required= False
    )

    error_messages = {
        'invalid_login' : (
            'username or password is/are incorect'
        ),
    }

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError('Type password!', code = 'invalid')
        return password
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError('Type username!', code = 'invalid')
        if not User.objects.filter(username = username):
            raise forms.ValidationError('There is no such user!', code = 'invalid')
        return username
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'country', 'city', 'street', 'building', 'appartmentNumber']

        widgets = {
            'gender': forms.Select(choices=Gender.choices),
        }
        
    