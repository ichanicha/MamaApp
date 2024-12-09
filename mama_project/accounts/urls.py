from django.urls import path
from .views import RegistUserView, UserLoginView, UserLogoutView

app_name = 'accounts'
urlpatterns = [
  path('regist/', RegistUserView.as_view(), name='regist'), #accounts/regist/でviews.pyのRegistViewを表示
  path('user_login/', UserLoginView.as_view(), name='user_login'), #accounts/user_login/でviews.pyのUserLoginViewを表示
  path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
]