from django.conf.urls import url
from clientapi import views

from django.conf.urls.static import static

urlpatterns = [
    url(r'^clientes/$', views.clientApi),
    url(r'^clientes/([0-9]+)$', views.clientApi),

]