from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")
    is_teacher = forms.BooleanField(required=False, help_text="Check if you are a teacher.")
    is_student = forms.BooleanField(required=False, help_text="Check if you are a student.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_teacher', 'is_student']

    def clean(self):
        cleaned_data = super().clean()
        is_teacher = cleaned_data.get("is_teacher")
        is_student = cleaned_data.get("is_student")

        if not is_teacher and not is_student:
            raise forms.ValidationError("You must select either Teacher or Student.")
        return cleaned_data

# Login Form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
