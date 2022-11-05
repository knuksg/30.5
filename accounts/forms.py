from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms
from django.forms import Textarea, TextInput


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "아이디",
            }
        ),
        label="",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "비밀번호",
            }
        ),
        label="",
    )


class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
        label=("아이디"),
        strip=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "아이디를 입력하세요",
            }
        ),
        help_text="",
    )
    password1 = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "placeholder": "비밀번호",
            }
        ),
        help_text="",
    )
    password2 = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "placeholder": "비밀번호 확인",
            }
        ),
        strip=False,
        help_text=(""),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password1",
            "password2",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "phone",
            "image",
        )
