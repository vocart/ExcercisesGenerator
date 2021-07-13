from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name = 'home'),
    path('train_generator/', views.train_generator, name = 'train_generator'),
    path('countdown/', views.countdown, name = 'countdown'),
    
    ]
