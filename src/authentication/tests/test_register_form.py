import pytest

from authentication.forms.register import RegisterForm
from authentication.models.user import User


@pytest.mark.django_db
@pytest.mark.parametrize(
    'username, password, confirm_password',
    [
        ('username', 'Password123@', 'Password123@'),
    ]
)
def test_register_form_valid(username, password, confirm_password):
    form = RegisterForm(data={'username': username, 'password': password, 'password_confirm': confirm_password})
    assert form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize(
    'username',
    [
        'user123',
        'user.name',
        'user@name',
        'user+name',
        'user-name',
        'user_name',
    ]
)
def test_register_form_valid_username(username):
    password = confirm_password = 'P@ssword123'
    form = RegisterForm(data={'username': username, 'password': password, 'password_confirm': confirm_password})
    assert form.errors.get('username', []) == []


@pytest.mark.django_db
@pytest.mark.parametrize(
    'username, message_error',
    [
        ('test_username', 'Tên tài khoản này đã được sử dụng.'),
    ]
)
def test_register_exists_username(username, message_error):
    password = confirm_password = 'P@ssword123'
    User.objects.create_user(username=username, password=password)  # type: ignore
    form = RegisterForm(data={'username': username, 'password': password, 'password_confirm': confirm_password})
    assert message_error in form.errors['username']


@pytest.mark.django_db
@pytest.mark.parametrize(
    'password', [
        'P@ssword123'
    ]
)
def test_register_form_valid_password(password):
    username = 'username'
    confirm_password = password
    form = RegisterForm(data={'username': username, 'password': password, 'password_confirm': confirm_password})
    assert form.errors.get('password', []) == []


@pytest.mark.django_db
@pytest.mark.parametrize(
    'password, message_error',
    [
        ('', 'Trường này là bắt buộc.'),
        ('short', 'Giá trị này phải có ít nhất 6 kí tự (hiện có 5)'),
        ('longpassword12345', 'Giá trị này chỉ có tối đa 16 kí tự (hiện có 17)'),
        ('password123', 'Mật khẩu phải có ít nhất một chữ in hoa.'),
        ('PASSWORD123', 'Mật khẩu phải có ít nhất một chữ in thường.'),
        ('Password', 'Mật khẩu phải có ít nhất một chữ số.'),
    ]
)
def test_invalid_password(password, message_error):
    username = 'username'
    confirm_password = password
    form = RegisterForm(data={'username': username, 'password': password, 'password_confirm': confirm_password})
    assert message_error in form.errors['password']


@pytest.mark.django_db
@pytest.mark.parametrize('password', [
    'P@ssword123'
])
def test_password_confirm_mismatch(password):
    username = 'username'
    confirm_password = password+'not_match'
    form = RegisterForm(data={'username': username, 'password': password, 'password_confirm': confirm_password})
    assert form.errors['password_confirm'] == ['Mật khẩu nhập lại không trùng khớp.']
