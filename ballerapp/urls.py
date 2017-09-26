
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from ballerapp.views import AdresseListView

app_nam= 'ballerapp'

urlpatterns = (
        
        url(r'^register/$', views.register_view, name='register'),
        url(r'^home/$', AdresseListView.as_view(), name='adresse-list-view'),
        url(r'^login/$', views.login_view, name='login'),
        url(r'^add_place/$', views.add_new_place, name='add_new_place'),
        url(r'^logout/$', views.logout_view, name='login'),
)
