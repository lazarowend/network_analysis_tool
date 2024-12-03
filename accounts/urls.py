from django.urls import path
from accounts.views import login, register


urlpatterns = [
    path('accounts/login/', login, name='login'),
    path('accounts/register/', register, name='register'),
]
