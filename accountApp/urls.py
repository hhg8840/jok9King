from django.urls import path

from accountApp.views import AccountCreateView

app_name = "accountApp"

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
]