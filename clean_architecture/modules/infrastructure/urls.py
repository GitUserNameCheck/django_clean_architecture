"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clean_architecture.modules.infrastructure.views import main_views, client_views, locations_views, event_views, employee_views, service_views, service_employee_views, event_service_employee_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.homepage, name='homepage'),
    path('register', main_views.register, name='register'),
    path('login', main_views.login, name='login'),
    path('personalCabin', main_views.personalCabin, name = 'personalCabin'),
    path('logout', main_views.logout, name='logout'),
    path('clients/', client_views.ClientListView.as_view(), name='clients'),
    path("client/create/", client_views.ClientCreateView.as_view(), name='client_create'),
    path("client/delete/<int:pk>", client_views.ClientDeleteView.as_view(), name='client_delete'),
    path("client/update/<int:pk>", client_views.ClientUpdateView.as_view(), name='client_update'),
    path('locations/', locations_views.LocationListView.as_view(), name='locations'),
    path("location/create/", locations_views.LocationCreateView.as_view(), name='location_create'),
    path("location/delete/<int:pk>", locations_views.LocationDeleteView.as_view(), name='location_delete'),
    path("location/update/<int:pk>", locations_views.LocationUpdateView.as_view(), name='location_update'),
    path('events/', event_views.EventListView.as_view(), name='events'),
    path("event/create/", event_views.EventCreateView.as_view(), name='event_create'),
    path("event/delete/<int:pk>", event_views.EventDeleteView.as_view(), name='event_delete'),
    path("event/update/<int:pk>", event_views.EventUpdateView.as_view(), name='event_update'),
    path('employees/', employee_views.EmployeeListView.as_view(), name='employees'),
    path("employee/create/", employee_views.EmployeeCreateView.as_view(), name='employee_create'),
    path("employee/delete/<int:pk>", employee_views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path("employee/update/<int:pk>", employee_views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('services/', service_views.ServiceListView.as_view(), name='services'),
    path("service/create/", service_views.ServiceCreateView.as_view(), name='service_create'),
    path("service/delete/<int:pk>", service_views.ServiceDeleteView.as_view(), name='service_delete'),
    path("service/update/<int:pk>", service_views.ServiceUpdateView.as_view(), name='service_update'),
    path('service_employees/', service_employee_views.ServiceEmployeeListView.as_view(), name='service_employees'),
    path("service_employee/create/", service_employee_views.ServiceEmployeeCreateView.as_view(), name='service_employee_create'),
    path("service_employee/delete/<int:pk>", service_employee_views.ServiceEmployeeDeleteView.as_view(), name='service_employee_delete'),
    path("service_employee/update/<int:pk>", service_employee_views.ServiceEmployeeUpdateView.as_view(), name='service_employee_update'),
    path('event_service_employees/', event_service_employee_views.EventServiceEmployeeListView.as_view(), name='event_service_employees'),
    path("event_service_employee/create/", event_service_employee_views.EventServiceEmployeeCreateView.as_view(), name='event_service_employee_create'),
    path("event_service_employee/delete/<int:pk>", event_service_employee_views.EventServiceEmployeeDeleteView.as_view(), name='event_service_employee_delete'),
    path("event_service_employee/update/<int:pk>", event_service_employee_views.EventServiceEmployeeUpdateView.as_view(), name='event_service_employee_update'),
]
