from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, UserDetailView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name="registration"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("user/<int:pk>/details/", UserDetailView.as_view(), name="user_detailed_view"),
]
