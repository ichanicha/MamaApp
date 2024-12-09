from django.db import models
from accounts.models import Users


class PostCountry(models.Model):
  COUNTRY = [
    ('1', '千種区'),
    ('2', '東区'),
    ('3', '北区'),
    ('4', '西区'),
    ('5', '中村区'),
    ('6', '中区'),
    ('7', '昭和区'),
    ('8', '瑞穂区'),
    ('9', '熱田区'),
    ('10', '中川区'),
    ('11', '港区'),
    ('12', '南区'),
    ('13', '守山区'),
    ('14', '緑区'),
    ('15', '名東区'),
    ('16', '天白区'),
    ]
  
  country = models.CharField(choices=COUNTRY, max_length=100)
  
  def __str__(self):
    # '千種区' などの表示名を返す
    return dict(self.COUNTRY).get(self.country, "不明")
  
  
class PostPictures(models.Model): #1対多で写真を紐づける
  image = models.ImageField(upload_to='image/', blank=True, null=True)
  oder = models.IntegerField(default=0)  # 順序用のフィールドを追加
  
  def __str__(self):
    return self.image.name 


class PostManager(models.Manager):
  def fetch_all_posts(self):
    return self.order_by('id').all()

class Post(models.Model):
  PARKING = [
    ('1', 'あり(無料)'),
    ('2', 'あり(有料)'),
    ('3', 'なし'),
    ('4', '不明'),
  ]
  BABY = [
      ('1', 'おむつ台・授乳室あり'),
      ('2', 'おむつ台あり'),
      ('3', '授乳室あり'),
      ('4', 'なし'),
      ('5', '不明'),
  ]
  
  user =  models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
  image = models.ForeignKey(PostPictures, on_delete=models.CASCADE)
  spot_name = models.CharField(max_length=50)
  country = models.ForeignKey(PostCountry, on_delete=models.CASCADE) #classPostCountryと紐づける
  address = models.CharField(max_length=100, null=True,blank=True)
  free = models.PositiveIntegerField(null=True,blank=True)
  parking = models.CharField(choices=PARKING, max_length=10)
  baby_station = models.CharField(choices=BABY, max_length=50)
  other = models.TextField(null=True,blank=True)
  create_at = models.DateTimeField(auto_now_add=True)  # 自動で作成日時を設定
  update_at = models.DateTimeField(auto_now=True)      # 自動で更新日時を設定
  
  objects = PostManager()
  
  class Meta:
    db_table = 'posts' #保存するテーブル名
    
  def __str__(self):
    return self.spot_name #spot_nameを返すように設定
