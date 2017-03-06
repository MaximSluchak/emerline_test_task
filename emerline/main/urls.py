from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^$', views.MainView.as_view())
]
