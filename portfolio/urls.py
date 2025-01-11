from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('gallery/', views.gallery, name='gallery'),  # Gallery page
    path('contact/', views.contact, name='contact'),  # Contact page
]