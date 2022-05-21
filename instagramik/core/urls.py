from distutils.log import Log
from django.urls import path
from .views import LoginView, logout_view, SignUpView, ProfileView, SubscribeView, ProfileUpdate

app_name = 'core'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('profile/<int:profile_id>/', ProfileView.as_view(), name='profile-detail'),
    path('subscribe/<int:user_id>', SubscribeView.as_view(), name='subscribe'),
    path('profile/<int:profile_id>/update/', ProfileUpdate.as_view(), name='profile-update')
]
