from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.views.generic.list import ListView 
from django.urls import reverse_lazy 

from .forms import PostForm, DeletePostForm 
from .models import Post, PostCountry 
from django.contrib.auth.mixins import LoginRequiredMixin 

import os

#投稿一覧
class ListView(LoginRequiredMixin, ListView): 
    template_name = 'list.html'
    model = Post
    context_object_name = 'posts'
    
    #商品絞り込み
    def get_queryset(self): 
      query = super().get_queryset()
      spot_name = self.request.GET.get('spot_name', None)
      country = self.request.GET.get('country', None)
      parking = self.request.GET.get('parking', None)
      baby_station = self.request.GET.get('baby_station', None) 

      if spot_name:
          query = query.filter(spot_name = spot_name)
      if country:
          query = query.filter(country = country)
      if parking:
          query = query.filter(parking = parking)
      if baby_station:
          query = query.filter(baby_station = baby_station)
      return query
  
    #検索内容を保持して表示
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        spot_name = self.request.GET.get('spot_name', '')
        country = self.request.GET.get('country', '')
        parking = self.request.GET.get('parking', '')
        baby_station = self.request.GET.get('baby_station', '')
        
        # クエリパラメータをコンテキストに設定
        context['spot_name'] = spot_name
        context['country'] = country
        context['parking'] = parking
        context['baby_station'] = baby_station
        
        # 動的に選択肢を作成
        context['country_choices'] = [(obj.id, obj.__str__()) for obj in PostCountry.objects.all()]
        context['parking_choices'] = Post.PARKING
        context['baby_station_choices'] = Post.BABY
        print(context['country_choices'])
        
        return context

#投稿作成ページ
class PostView(LoginRequiredMixin, CreateView):
    template_name = 'post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user # ログイン中のユーザーを投稿に関連付ける
        return super().form_valid(form)

# マイページ
class MyPageView(ListView):
    template_name = 'my_page.html'
    model = Post
    
    def get_queryset(self):
        # ログイン中のユーザーの投稿のみを表示
        return Post.objects.filter(user=self.request.user)
    
 
# 投稿編集ページ
def edit(request, id):
    post = get_object_or_404(Post, pk=id)  # 該当する投稿を取得
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) #データをformに格納
        if form.is_valid():
            form.save() # 既存の画像を保持または新しい画像を保存
            return redirect('posts:my_page')  # マイページにリダイレクト
    else:
        form = PostForm(instance=post)  # フォームに既存データを表示

    return render(request, 'edit.html', {'form': form, 'post': post})

# 削除確認ページ
def delete(request, id):
    post = get_object_or_404(Post, pk=id)  # 投稿を取得
    if request.method == 'POST':
        post.delete()  # 投稿を削除
        return redirect('posts:my_page')  # 削除後にマイページにリダイレクト
    return render(request, 'confirm_delete.html', {'post': post})  # 削除確認画面を表示
