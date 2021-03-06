from django.conf.urls import url
from . import views

app_name = 'datacarver'
urlpatterns = [
    # /datacarver/
    url(r'^$', views.index, name='index'),

    # /datacarver/<number>
    url(r'^(?P<filesig_id>[0-9]+)/$', views.detail, name='detail'),

    #/datacarver/recover
    url(r'^recover/$', views.recover, name='recover'),

    url(r'^add/$', views.addfile, name='addfsig'),

    url(r'^edit/$', views.editfile, name='editfsig'),

    url(r'^carvermenu/$', views.carverMenu, name='carvermenu'),

    url(r'^carvermain/$', views.carverMain, name='carvermain'),

]
