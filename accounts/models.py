from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveSmallIntegerField()

class Connect(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'following_user',
    )
    followed_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'followed_user',
    )
    created_at = models.DateTimeField(auto_now_add=True) # 登録タイムスタンプ
    updated_at = models.DateTimeField(auto_now=True) # 更新タイムスタンプ

    class Meta:
        unique_together = ['user', 'followed_user']

    def __str__(self):
        return str(self.user)
