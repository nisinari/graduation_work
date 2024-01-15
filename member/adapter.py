

# member/adapter.py

from allauth.account.adapter import DefaultAccountAdapter
from .models import *

class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)
        user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
        # user.userType = form.cleaned_data.get('userType')
        user.userType = UserType(request.POST['userType'])
        
        if not user.userType:
            user.userType = UserType(USERTYPE_DEFAULT) # デフォルトのユーザ種別を設定

        # ユーザIDを取得するために一旦保存する
        user.save()

        if int(user.userType.id) == USERTYPE_BUSINESS:
            # サプライヤーユーザ
            business = UserDetailBusiness()
            business.user_id = user.id
            business.companyName = request.POST['companyName']
            # business.serviceName = request.POST['serviceName']
            # business.created_at = request.POST['created_at']
            # business.updated_at = request.POST['updated_at']

            business.save()
        else:
            # それ以外は一般ユーザ
            user.userType = UserType(USERTYPE_BASIC)
            basic = UserDetailBasic()
            basic.user_id = user.id
            basic.accountName = request.POST.get('accountName', False)
            basic.userName = request.POST.get('userName', False)
            # basic.created_at = request.POST.get('created_at', False)
            # basic.updated_at = request.POST.get('updated_at')
            basic.save()
