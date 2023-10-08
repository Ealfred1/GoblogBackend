from django.urls import path

from . import views

urlpatterns = [
	path('', views.blog_overview, name='blog-overview'),
	path('blogs/', views.blogs, name='blogs'),
	path('create/', views.create_blog, name='create_blog'),
	path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
	path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
	path('delete/<int:blog_id>/', views.task_delete, name='task_delete'),
]