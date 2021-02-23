from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from accountApp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountApp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'accountApp/create.html'