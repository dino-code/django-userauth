from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
        exclude = ('password',)