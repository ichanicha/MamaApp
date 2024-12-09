from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import RegistForm, UserLoginForm


# ユーザー登録画面
class RegistUserView(CreateView):
    #CreateViewを利用したユーザー登録画面
    template_name = 'regist.html'
    form_class = RegistForm  # forms.pyのRegistFormを使用
    success_url = reverse_lazy("accounts:user_login")  # ユーザー登録後のリダイレクト先


# ログイン画面
class UserLoginView(LoginView):
    #ログイン画面
    template_name = 'user_login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        #フォームが有効な場合に実行
        remember = form.cleaned_data.get('remember')  # Remember meのデータを取得
        if remember:
            self.request.session.set_expiry(1200000)  # セッションの有効期限を設定
        return super().form_valid(form)


# ログアウト画面
class UserLogoutView(View):
    #ログアウト処理
    def get(self, request, *args, **kwargs):
        #GETリクエストを受けた際の処理
        logout(request)  # ログアウトを実行
        return redirect('accounts:user_login')  # ログイン画面にリダイレクト
