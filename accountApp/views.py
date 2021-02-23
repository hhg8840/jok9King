from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'accountApp/create.html'