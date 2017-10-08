from django.conf.urls import url
from . import views

urlpatterns = [
    # /datacarver/
    url(r'^$', views.index, name='index'),

    # /datacarver/<number>
    url(r'^(?P<filesig_id>[0-9]+)/$', views.detail, name='detail'),

    #/datacarver/recover
    url(r'^recover/$', views.recover, name='recover'),

]
