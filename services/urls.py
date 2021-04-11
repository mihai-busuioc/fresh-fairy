from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<services_id>', views.service_detail, name='service_detail'),

]
