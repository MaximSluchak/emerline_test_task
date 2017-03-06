from django import forms
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

from emerline.project.models import Project


class ProjectCreateForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=CheckboxSelectMultiple, required=False)

    class Meta:
        model = Project
        fields = ('projectName',)


class ProjectUpdateForm(forms.ModelForm):
    possible_users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=CheckboxSelectMultiple,
                                                    required=False)

    class Meta:
        model = Project
        fields = '__all__'
