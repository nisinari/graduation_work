from django.urls import path

from . import views

app_name = 'member'
urlpatterns = [
    path('signup_business/', views.SignUpBusinessView.as_view(), name='signup_business'),
    path('signup_basic/', views.SignUpBasicView.as_view(), name='signup_basic'),
]
