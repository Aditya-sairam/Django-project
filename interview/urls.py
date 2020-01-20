from django.contrib import admin
from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('interview/',PostListView.as_view(),name='interview-home'),
	path('interview/user/<str:username>',UserPostListView.as_view(),name='interview-posts'),
	path('interview/<int:pk>',PostDetailView.as_view(),name='interview-detail'),
	path('interview/<int:pk>/update',PostUpdateView.as_view(),name='interview-update'),
	path('interview/new',PostCreateView.as_view(),name='interview-create'),
	path('interview/<int:pk>/delete',PostDeleteView.as_view(),name='interview-delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


