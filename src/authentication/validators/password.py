import re

from django.core.exceptions import ValidationError


class CustomPasswordValidator:
    def validate(self, password, _=None):
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Mật khẩu phải có ít nhất một chữ in hoa.", code="password_no_upper")
        if not re.search(r'[a-z]', password):
            raise ValidationError("Mật khẩu phải có ít nhất một chữ in thường.", code="password_no_lower")
        if not re.search(r'\d', password):
            raise ValidationError("Mật khẩu phải có ít nhất một chữ số.", code="password_no_digit")

    def get_help_text(self):
        return "Mật khẩu phải chứa chữ in hoa, chữ in thường và chữ số."
