from django.contrib import admin

from .models import CustomUser,UserDetailBusiness,UserDetailBasic,UserType,UserManager


admin.site.register(CustomUser)
admin.site.register(UserDetailBusiness)
admin.site.register(UserDetailBasic)
admin.site.register(UserType)