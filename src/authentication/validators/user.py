import re

from django.forms import ValidationError


class CustomPasswordValidator():

    def __init__(self, min_length=6):
        self.min_length = int(min_length)

    def __call__(self, password):
        self.validate(password)

    def validate(self, password):
        if not password:
            raise ValidationError('Mật khẩu không được để trống.')
        if len(password) < 6:
            raise ValidationError('Mật khẩu quá ngắn. Mật khẩu phải chứa ít nhất 6 kí tự')
        if len(password) > 16:
            raise ValidationError('Mật khẩu quá dài. Mật khẩu chỉ được chứa tối đa 16 kí tự.')
        if password.isdigit():
            raise ValidationError('Mật khẩu này hoàn toàn là số. Vui lòng nhập lại mật khẩu khác.')
        if not any(char.isupper() for char in password):
            raise ValidationError("Mật khẩu chứa ít nhất một chữ in hoa.")

        if not any(char.islower() for char in password):
            raise ValidationError("Mật khẩu chứa ít nhất một chữ thường.")

        if not any(char.isdigit() for char in password):
            raise ValidationError("Mật khẩu chứa ít nhất một số.")

        if not re.search(r"[!@#$%^&*()?]", password):
            raise ValidationError("Mật khẩu chứa ít nhất một kí tự đặc biệt (!@#$%^&*()?).")

        if " " in password:
            raise ValidationError("Mật khẩu không được chứa khoảng cách.")

    def get_help_text(self):
        return (
            "chứa ít nhất một chữ in hoa, một chữ thường "
            "một số, một kí tự đặc biệt (!@#$%^&*()?), và không chứa khoảng trống."
        )
