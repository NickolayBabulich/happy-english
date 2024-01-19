from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import UserCreateView, UserDetailView, verify_email, UserUpdateView

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('user/register/', UserCreateView.as_view(), name='register'),
    path('user/profile/', UserDetailView.as_view(), name='profile'),
    path('user/edit/', UserUpdateView.as_view(), name='edit'),

    path('verify_email/<str:uidb64>/<str:token>/', verify_email, name='verify_email'),
]
