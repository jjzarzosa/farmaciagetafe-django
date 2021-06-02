from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Introduce un password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repite el password',
        'class': 'form-control',
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'movil','email','password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Introduce tu nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Introduce tus apellidos'
        self.fields['movil'].widget.attrs['placeholder'] = 'Introduce tu móvil'
        self.fields['email'].widget.attrs['placeholder'] = 'Introduce tu email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'