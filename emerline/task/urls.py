from django.conf.urls import url

from . import views

app_name = 'task'
urlpatterns = [
    url(r'^task/(?P<pk>\d+)$', views.TaskReadView.as_view()),
    url(r'^task/(?P<pk>\d+)/delete$', views.TaskDeleteView.as_view()),
    url(r'^task/new', views.create_task),
    url(r'^task/(?P<pk>\d+)/update$', views.TaskUpdateView.as_view()),
    url(r'^task/api/$', views.TaskList.as_view()),
    url(r'^task/api/new$', views.TaskCreate.as_view()),
    url(r'^task/api/(?P<pk>\d+)$', views.TaskDetail.as_view()),
]
