from django.conf.urls import url

from . import views

app_name = 'project'
urlpatterns = [
    url(r'^project/(?P<pk>\d+)$', views.ProjectReadView.as_view()),
    url(r'^project/(?P<pk>\d+)/delete$', views.ProjectDeleteView.as_view()),
    url(r'^project/new', views.create_project),
    url(r'^project/(?P<pk>\d+)/update$', views.ProjectUpdateView.as_view()),
    url(r'^project/api/$', views.ProjectList.as_view()),
    url(r'^project/api/new$', views.ProjectCreate.as_view()),
    url(r'^project/api/(?P<pk>\d+)$', views.ProjectDetail.as_view()),
]
