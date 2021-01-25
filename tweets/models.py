from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True) # 登録タイムスタンプ
    updated_at = models.DateTimeField(auto_now=True) # 更新タイムスタンプ