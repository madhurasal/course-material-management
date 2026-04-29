from operator import index
from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from .views import home, post,category,about


urlpatterns = [
    
    path('tinymce/', include('tinymce.urls')),
    path('home/', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category),
    path('about/', about),
    

]