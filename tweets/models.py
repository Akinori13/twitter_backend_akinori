from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.TextField(max_length=140)
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True) # 登録タイムスタンプ
    updated_at = models.DateTimeField(auto_now=True) # 更新タイムスタンプ

class Like(models.Model):
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['user', 'tweet'],
                name = 'user_tweet_unique'
            )
        ]
