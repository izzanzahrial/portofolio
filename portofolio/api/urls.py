from django.urls import path
from .views import BlogpostAPIView, BlogpostDetail

urlpatterns = [
    path('blogpost/', BlogpostAPIView.as_view()),
    path('blogpost/<int:pk>/', BlogpostDetail.as_view()),
]
