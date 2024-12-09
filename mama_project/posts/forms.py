from django import forms
from .models import Post, PostPictures

#投稿用のフォームクラス
class PostForm(forms.ModelForm):
  image_file = forms.ImageField(required=False) # 画像ファイルのアップロードフィールド（任意）

  # models.py の Post モデルと連携
  class Meta: 
    model = Post
    fields = ['spot_name','country','address','free','parking','baby_station','other']

    # フィールドごとにウィジェットをカスタマイズ（Bootstrapのスタイルを適用）
    widgets = {
      'spot_name': forms.TextInput(attrs={'class': 'form-control'}),
      'country': forms.Select(attrs={'class': 'form-control'}),
      'address': forms.TextInput(attrs={'class': 'form-control'}),
      'free': forms.NumberInput(attrs={'class': 'form-control'}),
      'parking': forms.Select(attrs={'class': 'form-control'}),
      'baby_station': forms.Select(attrs={'class': 'form-control'}),
      'other': forms.Textarea(attrs={'class': 'form-control'}),
    }
    
  #フォームを保存する際に画像を PostPictures モデルに保存し、Post モデルと関連付ける。
  def save(self, commit=True):
      # 画像を PostPictures モデルに保存
      image_file = self.cleaned_data.get('image_file') #アップロードされた画像ファイルを取得
      picture = None
      
      if image_file:
        # 新しい画像がアップロードされた場合、PostPictures モデルに保存
        picture = PostPictures.objects.create(image=image_file) 
      else:
         # 画像がアップロードされなかった場合、既存の画像を保持
        picture = self.instance.image
      
      # Post モデルのインスタンスを保存（まだデータベースには保存しない）
      instance = super().save(commit=False)
      if picture:
        instance.image = picture #新しい画像または既存の画像を関連付け
      if commit:
          instance.save() # データベースに保存
      return instance


#投稿削除用のフォームクラス
class DeletePostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = [] # フィールドなし（確認画面用）