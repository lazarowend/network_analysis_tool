from django.urls import path
from accounts.views import LoginView, RegisterView, home


urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login_view'),
    path('accounts/register/', RegisterView.as_view(), name='register_view'),
    path('home/', home, name='home'),

]
