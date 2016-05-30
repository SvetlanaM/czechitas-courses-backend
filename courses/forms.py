from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    """
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    username = forms.CharField(required = False)
    password1 = forms.CharField(required = False)
    password2 = forms.CharField(required = False)
    """

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', )

    """
    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user """