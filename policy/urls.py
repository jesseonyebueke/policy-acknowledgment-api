from django.urls import path

from . import views


urlpatterns = [
    path('current-policy/', views.current_policy, name='current-policy'),
    path('acknowledge/', views.acknowledge, name='acknowledge'),
]
