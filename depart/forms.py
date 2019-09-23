from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =('group_id', 'project_title', 'project_description', 'upload_file')