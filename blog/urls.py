from django.urls import include, path
from . import views
from .views import BlogCreateView

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', BlogCreateView.as_view(), name='make_blog'),
]