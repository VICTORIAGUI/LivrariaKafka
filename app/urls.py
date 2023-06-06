from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('ebook/', views.ebook, name='ebook'),
    path('infantil/', views.infantil, name='infantil'),
    path('importados/', views.importados, name='importados'),
<<<<<<< HEAD
    path('ofertas/', views.ofertas, name='ofertas'),
    path('quemsomos/', views.quemSomos, name='quemSomos'),
=======
    path('quemsomos/', views.quemSomos, name='quemSomos'),
    path('ofertas/', views.ofertas, name='ofertas')
>>>>>>> master
]
