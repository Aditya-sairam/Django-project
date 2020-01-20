from django.contrib import admin
from django.urls import path
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,userPostListView
from django.conf.urls.static import static
from django.conf import settings
from projects import views as project_views



urlpatterns = [
    path('project/', PostListView.as_view(),name='project-home'),
    path('project/user/<str:username>', userPostListView.as_view(),name='project-posts'),
    path('project/<int:pk>/', PostDetailView.as_view(),name='project-detail'),
    path('project/<int:pk>/update', PostUpdateView.as_view(),name='project-update'),
    path('project/new/', PostCreateView.as_view(),name='project-create'),
    path('project/<int:pk>/delete', PostDeleteView.as_view(),name='project-delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


