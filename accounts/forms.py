from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(
        label='年齢', 
        min_value=18, 
        help_text='18歳未満はご利用いただけません。'
        )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('age',)
