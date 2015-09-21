from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='home'),
    url(r'^setup$', views.setup, name='setup'),
    url(r'^database$', views.database, name='database'),
    url(r'^template$', views.template, name='template'),
]
