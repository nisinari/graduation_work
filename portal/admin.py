from django.contrib import admin

from .models import Company
from .models import Service
from .models import User
from .models import Post

admin.site.register(Company)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(Post)