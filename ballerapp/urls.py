
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from . import views

app_nam= 'ballerapp'

urlpatterns = (

        url(r'^register/$', views.register, name='register'),
        url(r'^home/$', views.index, name='index'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^add_place/$', views.add_new_place, name='add_new_place'),


)