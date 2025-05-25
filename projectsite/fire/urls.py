from django.urls import path
from . import views

urlpatterns = [
    # Locations
    path('locations/', views.LocationListView.as_view(), name='location-list'),
    path('locations/add/', views.LocationCreateView.as_view(), name='location-add'),
    path('locations/<int:pk>/edit/', views.LocationUpdateView.as_view(), name='location-edit'),
    path('locations/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='location-delete'),

    # Incidents
    path('incidents/', views.IncidentListView.as_view(), name='incident-list'),
    path('incidents/add/', views.IncidentCreateView.as_view(), name='incident-add'),
    path('incidents/<int:pk>/edit/', views.IncidentUpdateView.as_view(), name='incident-edit'),
    path('incidents/<int:pk>/delete/', views.IncidentDeleteView.as_view(), name='incident-delete'),

    # Fire Stations
    path('firestations/', views.FireStationListView.as_view(), name='firestation-list'),
    path('firestations/add/', views.FireStationCreateView.as_view(), name='firestation-add'),
    path('firestations/<int:pk>/edit/', views.FireStationUpdateView.as_view(), name='firestation-edit'),
    path('firestations/<int:pk>/delete/', views.FireStationDeleteView.as_view(), name='firestation-delete'),

    # Firefighters
    path('firefighters/', views.FirefightersListView.as_view(), name='firefighters-list'),
    path('firefighters/add/', views.FirefightersCreateView.as_view(), name='firefighters-add'),
    path('firefighters/<int:pk>/edit/', views.FirefightersUpdateView.as_view(), name='firefighters-edit'),
    path('firefighters/<int:pk>/delete/', views.FirefightersDeleteView.as_view(), name='firefighters-delete'),

    # Fire Trucks
    path('firetrucks/', views.FireTruckListView.as_view(), name='firetruck-list'),
    path('firetrucks/add/', views.FireTruckCreateView.as_view(), name='firetruck-add'),
    path('firetrucks/<int:pk>/edit/', views.FireTruckUpdateView.as_view(), name='firetruck-edit'),
    path('firetrucks/<int:pk>/delete/', views.FireTruckDeleteView.as_view(), name='firetruck-delete'),

    # Weather Conditions
    path('weatherconditions/', views.WeatherConditionsListView.as_view(), name='weatherconditions-list'),
    path('weatherconditions/add/', views.WeatherConditionsCreateView.as_view(), name='weatherconditions-add'),
    path('weatherconditions/<int:pk>/edit/', views.WeatherConditionsUpdateView.as_view(), name='weatherconditions-edit'),
    path('weatherconditions/<int:pk>/delete/', views.WeatherConditionsDeleteView.as_view(), name='weatherconditions-delete'),
] 