from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountApp.views import AccountCreateView

app_name = "accountApp"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
]