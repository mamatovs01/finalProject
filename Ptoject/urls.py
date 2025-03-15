from django.contrib import admin
from django.urls import path
from hz.views import *
# импорты статиков
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('browse/',browse,name="browse"),
    path('aboute/',about,name="about"),
    path('clients/',clients,name="clients"),
    path('contact/',contact,name="contact"),
    



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
