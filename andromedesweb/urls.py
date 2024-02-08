from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('business-cards', views.business_card, name='business-card'),
]