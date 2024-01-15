from django import forms

from allauth.account.forms import SignupForm
# from .validate import is_unique
from .models import CustomUser, UserDetailBusiness, UserDetailBasic, UserType

class SignUpBusinessForm(SignupForm):
    companyName = forms.CharField(max_length=30, label='事業者名(必須)')
    # serviceName = forms.CharField(max_length=30, label='サービス名（必須）')
    # introduction = forms.CharField(max_length=100, label='サービス紹介')
    # thumbnail = forms.ImageField(label='サムネイル', required=False)
    # image = forms.ImageField(label='自社ページ用画像', required=False)
    # category = forms.CharField(max_length=100, label='カテゴリー', required=False)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['userType'].widget = forms.HiddenInput()

    def save(self, request):
        user = super(SignUpBusinessForm, self).save(request)
        user.userType = request.POST['userType']
        user.save()
        return user

class SignUpBasicForm(SignupForm):
    userName = forms.CharField(max_length=30, label='利用者名(必須)')
    # accountName = forms.CharField(max_length=30, label='アカウント名（必須）')
    # introduction = forms.CharField(max_length=100, label='自己紹介')

    def save(self, request):
        user = super(SignUpBasicForm, self).save(request)
        user.userType = request.POST['userType']
        user.save()
        return user