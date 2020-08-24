from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile
from imagekit.forms import ProcessedImageField

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
        help_texts = {
            'username': '실명으로 입력하세요',
        }
        exclude = ['password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['student_no']
        widgets = {
            'student_no' : forms.TextInput(attrs={'class': 'form-control ','placeholder': '학번'}),
        }
        labels = {
            'student_no' : '학번',
        }
        help_texts = {
            'student_no': '틀리지않게 주의하세요',
        }
        
        