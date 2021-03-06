from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    # これを追加
    def __str__(self):
        return u'{}'.format(self.title) # オブジェクトのtitleの部分を表示するように設定
