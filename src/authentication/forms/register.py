from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator

from authentication.models import User
from authentication.validators.user import CustomPasswordValidator


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=32, validators=[UnicodeUsernameValidator()])
    password = forms.CharField(validators=[CustomPasswordValidator()])
    password_confirm = forms.CharField()

    def clean_username(self):
        username: str = self.cleaned_data['username']

        username = username.lower()

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Tên tài khoản này đã được sử dụng.')

        return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data['password_confirm']

        if password and password != password_confirm:
            raise forms.ValidationError('Mật khẩu nhập lại không trùng khớp.')

        return password_confirm
