from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializer import PostSerializer


@api_view(['GET'])
def blog_overview(request):
	api_urls = {
		'List': '/task-list/',
		'Detail': '/task-detail/<str:pk>',
		'Create': '/task-create/',
		'Update': '/task-update/<str:pk>',
		'Delete': '/task-delete/<str:pk>',
	}
	return Response(api_urls)


@api_view(['GET'])
def blogs(request):
  blogs = BlogPost.objects.all()
  serializer = PostSerializer(blogs, many=True)
  
  return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, blog_id):
  blog = get_object_or_404(BlogPost, id=blog_id)
  serializer = PostSerializer(blog, many=False)
  
  return Response(serializer.data)


@api_view(['POST'])
def create_blog(request):
  serializer = PostSerializer(data=request.data)
  
  if serializer.is_valid():
    serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def edit_blog(request, blog_id):
  blog = get_object_or_404(BlogPost, id=blog_id)
  serializer = PostSerializer(instance=blog, data=request.data)
  
  if serializer.is_valid():
    serializer.save()
  
  return Response(serializer.data)
  

@api_view(['DELETE'])
def task_delete(request, blog_id):
	blog = get_object_or_404(BlogPost, id=blog_id)
	blog.delete()
	
	return Response('Blog Deleted Successfully')

