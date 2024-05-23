from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:name>', views.main, name='main'),
    path('track/', views.track_user_view, name='track_user'),
]