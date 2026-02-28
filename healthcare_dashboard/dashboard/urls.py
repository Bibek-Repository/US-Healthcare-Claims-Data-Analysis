from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-claim/', views.add_claim, name='add_claim'),
]