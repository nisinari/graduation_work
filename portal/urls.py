from django.urls import path

from . import views


app_name = 'portal'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    # service_listはindexを参照
    # path('service-list/', views.ServiceListView.as_view(), name="service_list"),
    path('index/', views.IndexView.as_view(), name="service_list"),

    path('<int:pk>/', views.ServiceDetailView.as_view(), name="service_detail"),
    # path('service-detail/<int:pk>/', views.ServiceDetailView.as_view(), name="service_detail"),
    # path('service-detail/<str:name>/', views.ServiceDetailView.as_view(), name="service_detail"),
    path('service-create/', views.ServiceCreateView.as_view(), name="service_create"),
    path('service-update/<int:pk>/', views.ServiceUpdateView.as_view(), name="service_update"),
    path('service-delete/<int:pk>/', views.ServiceDeleteView.as_view(), name="service_delete"),
    # post_listはservice_detailを参照
    # path('post-list/', views.PostListView.as_view(), name="post_list"),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post-create/', views.PostCreateView.as_view(), name="post_create"),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name="post_update"),
    path('post-delete/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),

    path('search-result/<int:pk>/', views.SearchResultView.as_view(), name="search_result"),


    # path('login/', views.CompanyLogInView.as_view(), name="login"),
    # path('signup/', views.CompanySignUpView.as_view(), name="signup"),
    # path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    # path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    # path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
]
