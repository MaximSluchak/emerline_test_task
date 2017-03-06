from django.contrib.auth.decorators import permission_required
from django.forms import modelform_factory, CheckboxSelectMultiple
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from rest_framework import generics

from emerline.project.models import Project
from emerline.project.forms import ProjectCreateForm
from emerline.user.serializers import ProjectSerializer


@permission_required('project.add_project')
def create_project(request):
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            project = Project.objects.create(projectName=form.cleaned_data['projectName'])
            project.save()
            project.users.add(request.user)
            project.users.add(*form.cleaned_data['users'])
            return redirect("/")
    else:
        form = ProjectCreateForm()

    return render(request, 'project/create_project.html', {'form': form})


class ProjectReadView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'

    @method_decorator(permission_required('project.view_project'))
    def dispatch(self, *args, **kwargs):
        return super(ProjectReadView, self).dispatch(*args, **kwargs)


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = modelform_factory(
        Project, widgets={'users': CheckboxSelectMultiple}, fields='__all__'
    )
    template_name = 'update.html'
    success_url = '/'

    @method_decorator(permission_required('project.change_project'))
    def dispatch(self, *args, **kwargs):
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/"

    @method_decorator(permission_required('project.delete_project'))
    def dispatch(self, *args, **kwargs):
        return super(ProjectDeleteView, self).dispatch(*args, **kwargs)


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
