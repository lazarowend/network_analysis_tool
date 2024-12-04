from django.urls import path
from accounts.views import LoginView, RegisterView, LogoutView, SocialAccountListView


urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login_view'),
    path('accounts/register/', RegisterView.as_view(), name='register_view'),
    path('accounts/logout/', LogoutView.as_view(), name='logout_view'),
    path('accounts/social_accounts/', SocialAccountListView.as_view(), name='social_account_list_view'),
]
