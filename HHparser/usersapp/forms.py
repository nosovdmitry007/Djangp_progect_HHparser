from django.contrib.auth.forms import UserCreationForm
from .models import ParserUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = ParserUser
        fields = ('username', 'password1', 'password2', 'email')