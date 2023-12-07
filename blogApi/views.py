from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import *
from .models import Post
from .serializer import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


#  Users

class UserList(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserRegistration(CreateAPIView):
	serializer_class = UserRegistrationSerializer


class UserLogin(APIView):
	def post(self, request):
		data = request.data
		serializer = LoginSerializer(data=data)
		
		if serializer.is_valid():
			username = serializer.data['username']
			password = serializer.data['password']
			
			user = authenticate(request,username=username, password=password)
			
			if user is not None:
				refresh = RefreshToken.for_user(user)
				user_serializer = UserSerializer(user)
				return Response({
					'refresh': str(refresh),
					'access': str(refresh.access_token),
					#'user': f'{user.first_name} {user.last_name}',
					'user': user_serializer.data
				})
			return Response({
				'message': 'Invalid Credentials'
			})
		
		return Response({
			'message': 'Something went wrong',
			'data': serializer.errors
		})

# Posts

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
  #  permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
