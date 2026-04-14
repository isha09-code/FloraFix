# diagnosis/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Empty string '' → matches the project prefix /diagnose/
    path('', views.index, name='diagnose'),
    path('api/predict/', views.predict_api, name='predict_api'),
]
