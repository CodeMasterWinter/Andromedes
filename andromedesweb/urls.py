from django.urls import path
from . import views

urlpatterns = [
    path('business-cards', views.business_card, name='business-card'),
]