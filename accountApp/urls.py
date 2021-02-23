from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountApp.views import AccountCreateView, hello_world

app_name = "accountApp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='accountApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
]