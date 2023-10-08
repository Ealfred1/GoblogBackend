from .models import BlogPost
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogPost
		fields = '__all__'