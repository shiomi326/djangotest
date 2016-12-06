from django.conf.urls import url
from forum import views  # 先ほど作成したビューをインポート。（正確にはviews.pyファイル内のすべてのものをインポート）


# URLパターンのリストに新しいURLを追加
urlpatterns = [
    url(r'post/create/$', views.PostCreate.as_view(), name='post_create'),
]
