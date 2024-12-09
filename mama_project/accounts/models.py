from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin,
)
from django.urls import reverse_lazy


class UserManager(BaseUserManager):
    #ユーザー作成用マネージャークラス
    def create_user(self, username, email, password=None):
        #通常のユーザーを作成
        if not email:
            raise ValueError('メールアドレスを入力してください')
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        #スーパーユーザーを作成
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    #カスタムユーザーモデル
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)  # デフォルトで有効
    is_staff = models.BooleanField(default=False)  # スタッフ権限

    # 認証に使用するフィールド
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # 必須フィールド

    # カスタムマネージャーを設定
    objects = UserManager()

    def get_absolute_url(self):
        #ユーザー作成後のリダイレクトURL
        return reverse_lazy('accounts:user_login')
