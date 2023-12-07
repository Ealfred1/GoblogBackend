from django.urls import path

from .views import *

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
	# Users and Auth
	path('users/', UserList.as_view()),
	path('user/<int:pk>', UserDetail.as_view()),
	path('register/', UserRegistration.as_view()),
	path('token/', UserLogin.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Posts
    
    path('posts/', PostList.as_view()),
    path('post/<int:pk>', PostDetail.as_view())
]