from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^user/(?P<pk>\d+)$', views.DeveloperReadView.as_view()),
    url(r'^user/(?P<pk>\d+)/delete$', views.DeveloperDeleteView.as_view()),
    url(r'^user/new', views.create_developer),
    url(r'^user/(?P<pk>\d+)/update$', views.DeveloperUpdateView.as_view()),
    url(r'^user/api/$', views.UserList.as_view()),
    url(r'^user/api/new$', views.UserCreate.as_view()),
    url(r'^user/api/(?P<pk>\d+)$', views.UserDetail.as_view()),
]
