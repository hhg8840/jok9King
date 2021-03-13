from django.forms import ModelForm

from projectApp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description']