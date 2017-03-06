from django.contrib.auth.forms import UserCreationForm
from django import forms

ROLES = (
    ('developer', 'developer'),
    ('manager', 'manager'),
)


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLES)
