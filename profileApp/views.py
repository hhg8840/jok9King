from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileApp.decorators import profile_ownership_required
from profileApp.forms import ProfileCreationForm
from profileApp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'profileApp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False) #임시데이터
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountApp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'profileApp/update.html'

    def get_success_url(self):
        return reverse('accountApp:detail', kwargs={'pk': self.object.user.pk})