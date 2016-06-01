from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrar/$', views.respondePreguntas, name='registrarUsuario'),
    url(r'^voteBoard/$', views.voteBoard, name='voteBoard'),
    url(r'^usuarioVota/$', views.usuarioVota, name='usuarioVota'),

]
