from django import forms
from django.contrib.auth.models import User

from emerline.project.models import Project
from emerline.task.models import Task


class TaskCreateForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    developer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='developer'), required=False)
    dueDate = forms.DateTimeField()

    class Meta:
        model = Task
        fields = ('title', 'description', )
