from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<int:services_id>/', views.service_detail, name='service_detail'),
    path('add_service', views.add_service, name='add_service'),
    path('edit/<int:services_id>/', views.edit_service, name='edit_service'),
    path('delete/<int:services_id>/', views.delete_service,
         name='delete_service'),

]
