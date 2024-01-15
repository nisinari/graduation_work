from django.db import models
from member.models import CustomUser

class Company(models.Model):
    name = models.ForeignKey(CustomUser,verbose_name='事業者名', on_delete=models.PROTECT)
    # name = models.CharField(verbose_name='事業者名', max_length=40)
    # mail_address = models.CharField(verbose_name='メールアドレス', max_length=40)
    account = models.CharField(verbose_name='アカウント名', max_length=40)
    password = models.CharField(verbose_name='パスワード', max_length=40)
    introduction = models.TextField(verbose_name='サービス紹介')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.name

SERVICE_TYPES =(
        # (データベースに保存される値, フォームウィジェットに表示される値),
        ('space', '空間'),
        ('stuff', 'モノ'),
        ('transportation', '移動'),
        ('skill', 'スキル'),
    )
class Service(models.Model):
    company = models.ForeignKey(CustomUser,verbose_name='事業者',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='サービス名', max_length=40)
    overview = models.TextField(verbose_name='概要')
    image = models.ImageField(verbose_name='画像', blank=True, null=True)
    thumbnail = models.ImageField(verbose_name='サムネイル', blank=True, null=True)
    category = models.CharField(verbose_name='カテゴリ',choices=SERVICE_TYPES, max_length=40)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Service'

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.ForeignKey(CustomUser, verbose_name='利用者', on_delete=models.PROTECT)
    # name = models.CharField(verbose_name='利用者', max_length=40)
    # mail_address = models.CharField(verbose_name='メールアドレス', max_length=40)
    account = models.CharField(verbose_name='アカウント名', max_length=40)
    password = models.CharField(verbose_name='パスワード', max_length=40)
    introduction = models.TextField(verbose_name='自己紹介', null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'User'

    def __str__(self):
        return self.name

class Post(models.Model):
    service = models.ForeignKey(Service, verbose_name='サービス',on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='投稿者',on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    body = models.TextField(verbose_name='内容')
    price = models.CharField(verbose_name='価格', max_length=40)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.title