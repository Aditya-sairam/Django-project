from django.contrib import admin
from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,userPostListView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', userPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('about/', views.About,name='blog-about'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
    path('softskills/',views.Soft,name='softskills'),


    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)