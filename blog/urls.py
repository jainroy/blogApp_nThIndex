from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListAPIView.as_view(), name="blogs"),
    path('<int:id>/', views.BlogDetailAPIView.as_view(), name="blog-detail"),
    path('report/', views.ReportUserAPIView.as_view(), name='report-blog'),
    path('all-blogs/', views.blogListView, name='all-blogs'),
]
