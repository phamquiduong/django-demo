import pytest

from authentication.forms.register import RegisterForm
from authentication.models.user import User


@pytest.mark.django_db
@pytest.mark.parametrize(
    'username,password,confirm_password',
    [
        ('username1', 'username123@', 'username123@'),
    ]
)
def test_register_form_valid(username, password, confirm_password):
    form = RegisterForm(data={'username': username, 'password': password, 'password_confirm': confirm_password})
    assert form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize('username', [
    'user123',
    'user.name',
    'user@name',
    'user+name',
    'user-name',
    'user_name',
])
def test_register_form_valid_username(username):
    form = RegisterForm(
        data={
            'username': username,
            'password': 'P@ssTest123',
            'password_confirm': 'P@ssTest123',
        }
    )

    assert form.is_valid(), form.errors['username']


@pytest.mark.django_db
@pytest.mark.parametrize('username', [
    'test_username'
])
def test_register_exists_username(username):
    User.objects.create_user(username=username, password='P@ssTest123')

    form = RegisterForm(
        data={
            'username': username,
            'password': 'P@ssTest123',
            'password_confirm': 'P@ssTest123',
        }
    )

    assert form.is_valid() is False
    assert form.errors['username'] == ['Tên tài khoản này đã được sử dụng.']


@pytest.mark.django_db
@pytest.mark.parametrize('password', [
    'P@ssword123'
])
def test_register_form_valid_password(password):
    form = RegisterForm(
        data={
            'username': 'username',
            'password': password,
            'password_confirm': password,
        }
    )

    assert form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize(
    'password, confirm_password, expected_errors',
    [
        ('short', 'short', ['This password is too short. It must contain at least 6 characters.']),

        ('45612389464', '45612389464', ['Mật khẩu này hoàn toàn là số.']),

        ('password', 'password', ['Mật khẩu này quá phổ biến.']),
    ]
)

def test_invalid_password(password, confirm_password, expected_errors):
    form = RegisterForm(data={
        'username': 'test_user',
        'password': password,
        'password_confirm': confirm_password,
    })
    assert form.is_valid() is False
    assert form.errors['password'] == expected_errors


@pytest.mark.django_db
@pytest.mark.parametrize('password', [
    'P@ssword123'
])
def test_password_confirm_mismatch(password):
    form = RegisterForm(
        data={
            'username': 'username',
            'password': password,
            'password_confirm': password+'not_match',
        }
    )

    assert form.is_valid() is False
    assert form.errors['password_confirm'] == ['Mật khẩu nhập lại không trùng khớp.']
