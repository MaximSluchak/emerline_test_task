from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from rest_framework import generics

from emerline.main.views import DEVELOPER_PERMISSIONS
from emerline.user.forms import DeveloperCreateForm
from emerline.user.serializers import UserSerializer


@permission_required('auth.add_user')
def create_developer(request):
    if request.method == 'POST':
        form = DeveloperCreateForm(request.POST)
        if form.is_valid():
            developer = User.objects.create_user(username=form.cleaned_data['username'],
                                                 password=form.cleaned_data['password1'],
                                                 email=form.cleaned_data['email'])
            group, created = Group.objects.get_or_create(name='developer')
            if created:
                permissions = [Permission.objects.get(codename=codename) for codename in DEVELOPER_PERMISSIONS]
                group.permissions.add(*permissions)
            developer.groups.add(group)
            developer.save()
            # email = EmailMessage('11', '22', to=['sluchak1995@gmail.com'])
            # email.send()
            return redirect("/")
    else:
        form = DeveloperCreateForm()

    return render(request, 'user/create_developer.html', {'form': form})


class DeveloperReadView(DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def dispatch(self, *args, **kwargs):
        return super(DeveloperReadView, self).dispatch(*args, **kwargs)


class DeveloperUpdateView(UpdateView):
    model = User
    template_name = 'update.html'
    fields = ('username', 'email',)
    success_url = '/'

    @method_decorator(permission_required('auth.change_user'))
    def dispatch(self, *args, **kwargs):
        return super(DeveloperUpdateView, self).dispatch(*args, **kwargs)


class DeveloperDeleteView(DeleteView):
    model = User
    success_url = "/"

    @method_decorator(permission_required('auth.delete_user'))
    def dispatch(self, *args, **kwargs):
        return super(DeveloperDeleteView, self).dispatch(*args, **kwargs)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
