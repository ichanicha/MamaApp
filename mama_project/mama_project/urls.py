from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # accounts/urls.pyへつなげる処理
    path('posts/', include('posts.urls')),  # posts/urls.pyへつなげる処理
]

# 開発環境でのみ静的ファイルやメディアファイルのURL設定を行う
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
