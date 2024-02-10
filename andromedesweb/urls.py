from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('business-card', views.business_card, name='business-card'),
    path('business-cards', views.business_cards, name='business-cards'),
]