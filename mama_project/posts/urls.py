from django.urls import path
from .views import PostView, ListView, MyPageView, edit, delete

app_name = 'posts'

urlpatterns = [
    # 投稿作成ページ
    path('post/', PostView.as_view(), name='post'),
    
    # 投稿一覧ページ
    path('list/', ListView.as_view(), name='list'),
    
    # マイページ
    path('my_page/', MyPageView.as_view(), name='my_page'),
    
    # 投稿編集ページ
    path('edit/<int:id>/', edit, name='edit'),
    
    # 投稿削除ページ
    path('delete/<int:id>/', delete, name='delete'),
]
