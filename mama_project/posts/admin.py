from django.contrib import admin
from .models import (PostCountry,Post, PostPictures)

admin.site.register(
  [PostCountry, Post, PostPictures]
)
