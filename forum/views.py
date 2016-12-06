from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView  # DjangoのCreateViewをインポート
from django.core.urlresolvers import reverse_lazy
from forum.models import Post  # 先ほど作成したデータベースモデルのPostをインポート


class PostCreate(CreateView):  # CreateViewを基に新しいクラスを定義。基底クラスに定義されている機能をすべて継承
    model = Post  # 使用するモデルを定義
    fields = ['title', 'body']  # フォームで編集可能にするモデルフィールド

    def get_success_url(self):
        return reverse_lazy('post_create')  # フォームを投稿後の飛び先を指定
