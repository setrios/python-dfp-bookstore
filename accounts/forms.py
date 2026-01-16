from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # always use this to get user model from settings.py
        fields = (
            'email',
            'username'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()  # always use this to get user model from settings.py
        fields = (
            'email',
            'username'
        )