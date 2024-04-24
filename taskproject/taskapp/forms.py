from django import forms
from .models import User, Task
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile']

    def validate_email(self):
        email = self.cleaned_data.get('email')
        validate_email(email)
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with this email already exists.')
        return email
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'detail', 'status']