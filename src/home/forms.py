from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class UserForm(ModelForm):

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError(
                'El nombre es requerido.'
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError(
                'El apellido es requerido.'
            )
        return last_name

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
        )
