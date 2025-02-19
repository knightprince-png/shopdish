from django.contrib import admin
from django.urls import path
from shopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.images, name='gallery'),
    path('about/', views.about, name='about'),
]
