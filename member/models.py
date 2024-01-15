
# member/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager

USERTYPE_BUSINESS = 1
USERTYPE_BASIC = 2
USERTYPE_DEFAULT = USERTYPE_BASIC

class UserType(models.Model):
    """ ユーザ種別 """
    typename = models.CharField(verbose_name='ユーザ種別',
                                max_length=150)
    def __str__(self):
        return f'{self.id} - {self.typename}'

class CustomUserManager(UserManager):
    """ 拡張ユーザーモデル向けのマネージャー """

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """ 拡張ユーザーモデル """

    class Meta(object):
        db_table = 'custom_user'

    #作成したマネージャークラスを使用
    objects = CustomUserManager()

    # モデル内にユーザ種別を持つ
    userType = models.ForeignKey(UserType,
                                verbose_name='ユーザ種別',
                                null=True,
                                blank=True,
                                on_delete=models.PROTECT)
    def __str__(self):
        return self.username

class UserDetailBusiness(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_business',
                                on_delete=models.CASCADE)
    # 事業者向けの項目
    companyName = models.CharField(max_length=100)
    # # slugに利用、重複不可
    # serviceName = models.CharField(max_length=100,default='')
    # introduction = models.TextField(max_length=100, null=True, blank=True,default='')
    # thumbnail = models.ImageField(verbose_name='サムネイル', null=True, blank=True)
    # # Image = models.ImageField(verbose_name='自社ページ用画像', null=True, blank=True)
    # category = models.CharField(max_length=100, null=True, blank=True,default='')
    # created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    # updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    
    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{user.id} - {user.username} - {user.email} - {self.id} - {self.companyName}'
        # user = CustomUser.objects.get(pk=self.user.pk)
        # return f'{user.pk} - {user.username} - {user.email} - {self.pk} - {self.companyName}'

class UserDetailBasic(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_basic',
                                on_delete=models.CASCADE)
    # 通常利用者向けの項目
    userName = models.CharField(max_length=100, default='')
    # accountName = models.CharField(max_length=100)
    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
    #     return f'{user.id} - {user.username} - {user.email} - {self.id} - {self.accountName}'
    # introduction = models.TextField(max_length=100, null=True, blank=True,)
    # created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    # updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)