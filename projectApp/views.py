from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView  #, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articleApp.models import Article
from projectApp.forms import ProjectCreationForm
from projectApp.models import Project
from subscribeApp.models import Subscription


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectApp/create.html'

    def get_success_url(self):
        return reverse('projectApp:detail', kwargs={'pk': self.object.pk})


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectApp/list.html'
    paginate_by = 25


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectApp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None

        object_list = Article.objects.filter(project=self.get_object())

        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)


# class ProjectDeleteView(DeleteView):
#     model = Project
#     context_object_name = 'target_project'
#     template_name = 'projectApp/delete.html'
#     success_url = reverse_lazy('projectApp:list')
