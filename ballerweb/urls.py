from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from ballerapp import views
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    #url(r'^ballerapp/', include('ballerapp.urls')),
   # url(r'^register/$', views.register, name='register'),
   # url('^register/', include('django.contrib.auth.urls) ),
    url(r'^ballerweb/', include('ballerapp.urls'), name="ballerweb"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
