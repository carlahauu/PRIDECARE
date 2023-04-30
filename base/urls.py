from django.contrib import admin
from django.urls import path
from .views import search, home, form
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.search , name='search'),
    path('', views.home , name='home'),
    path('form', views.form , name='form'),
]