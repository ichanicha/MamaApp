from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm


class RegistForm(forms.ModelForm):
    #ユーザー登録フォーム
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        #パスワードの暗号化処理とユーザー保存
        user = super().save(commit=False)  # 親クラスの save メソッドをカスタマイズ
        validate_password(self.cleaned_data['password'], user)  # パスワードバリデーション
        user.set_password(self.cleaned_data['password'])  # 暗号化したパスワードを設定
        if commit:
            user.save()  # データベースに保存
        return user


class UserLoginForm(AuthenticationForm):
    #ログインフォーム
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    remember = forms.BooleanField(label='ログイン状態を保持する', required=False)
