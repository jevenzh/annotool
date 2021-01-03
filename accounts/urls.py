from django.urls import path

from django.contrib.auth import views as auth_views
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('login/', LoginView.as_view(), name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]