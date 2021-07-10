from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),

    path('commercial/', views.commercial_view, name='commercial'),
    path('commercial/<int:sno>', views.commercial_single_view,
         name='commercial_single'),

    path('residential/', views.residential_view, name='residential'),
    path('residential/<int:sno>', views.residential_single_view,
         name='residential_single'),

    path('add_comm_property/', views.addcommproperty_view,
         name='add_comm_property'),
    path('add_resi_property/', views.addresiproperty_view,
         name='add_resi_property'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('delete/<int:sno>', views.delete_comm_view, name="delete_comm"),
    path('deleteresi/<int:sno>', views.delete_resi_view, name="delete_resi"),

]
