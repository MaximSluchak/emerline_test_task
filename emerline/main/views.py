from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Permission, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView
from django.views.generic import ListView

from emerline.main.forms import CustomRegistrationForm
from emerline.project.models import Project
from emerline.task.models import Task

MANAGER_PERMISSIONS = {
    'add_task',
    'delete_task',
    'change_task',
    'view_task',
    'add_project',
    'delete_project',
    'change_project',
    'view_project',
    'add_user',
    'change_user',
    'delete_user',
}

DEVELOPER_PERMISSIONS = {
    'view_task',
    'view_project',
}


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])
            role = form.cleaned_data['role']
            group, created = Group.objects.get_or_create(name=form.cleaned_data['role'])
            if created:
                if role == 'manager':
                    permissions = [Permission.objects.get(codename=codename) for codename in MANAGER_PERMISSIONS]
                if role == 'developer':
                    permissions = [Permission.objects.get(codename=codename) for codename in DEVELOPER_PERMISSIONS]
                group.permissions.add(*permissions)
            user.groups.add(group)
            user.save()
            return redirect("/login", {'form': AuthenticationForm()})
    else:
        form = CustomRegistrationForm()

    return render(request, 'main/register.html', {'form': form})


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "main/login.html"

    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class MainView(ListView):
    model = User
    template_name = 'main/main.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(MainView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['is_developer'] = self.request.user.groups.filter(name='developer').exists()
        context['is_manager'] = self.request.user.groups.filter(name='manager').exists()
        context['has_tasks'] = self.request.user.task_set.exists()
        context['all_tasks'] = Task.objects.all()
        context['all_projects'] = Project.objects.all()
        return context
