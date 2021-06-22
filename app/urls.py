from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name='index'),
    path('home/', views.home_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
