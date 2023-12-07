from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView



class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name', 'email', 'username', 'posts']
		

class PostSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	
	class Meta:
		model = Post
		fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
	
	password = serializers.CharField(write_only=True)
	
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
		
	def create(self,validated_data):
		user = User.objects.create_user(
			username = validated_data['username'], 
			first_name=validated_data['first_name'],
		    last_name=validated_data['last_name'], 
		    email=validated_data['email'], 
		    password=validated_data['password']
		   )
		return user


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()