from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='home'),  # Home page now points to the gallery view
    path('about/', views.about, name='about'),  # About page
    path('gallery/', views.gallery, name='gallery'),  # Gallery page (also accessible via /gallery/)
    path('contact/', views.contact, name='contact'),  # Contact page
]