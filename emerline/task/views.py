from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from rest_framework import generics

from emerline.task.forms import TaskCreateForm
from emerline.task.models import Task


from emerline.user.serializers import TaskSerializer


@permission_required('task.add_task')
def create_task(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(title=form.cleaned_data['title'],
                                       dueDate=form.cleaned_data['dueDate'],
                                       description=form.cleaned_data['description'],
                                       user=form.cleaned_data['developer'],
                                       projects=form.cleaned_data['project'])
            task.save()
            return redirect("/")
    else:
        form = TaskCreateForm()

    return render(request, 'task/create_task.html', {'form': form})


class TaskReadView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'

    @method_decorator(permission_required('task.view_task'))
    def dispatch(self, *args, **kwargs):
        return super(TaskReadView, self).dispatch(*args, **kwargs)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    fields = '__all__'
    success_url = '/'

    @method_decorator(permission_required('task.change_task'))
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task

    success_url = "/"

    @method_decorator(permission_required('task.delete_task'))
    def dispatch(self, *args, **kwargs):
        return super(TaskDeleteView, self).dispatch(*args, **kwargs)


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
