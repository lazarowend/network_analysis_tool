from django.urls import path
from accounts.views import login


urlpatterns = [
    path('accounts/login/', login, name='login'),
]
