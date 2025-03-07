from django.urls import path
from core.views.user_views import home, register_user, login_user, logout_user

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),  # Map the root URL to the home view
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
