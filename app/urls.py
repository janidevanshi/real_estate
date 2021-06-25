from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('commercial/', views.commercial_view, name='commercial'),
    path('commercial/<str:slug>', views.commercial_single_view,
         name='commercial_single'),
    # path('residential/', views.residential_view, name='residential'),
]
