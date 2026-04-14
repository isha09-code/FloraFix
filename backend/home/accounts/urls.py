from django.urls import path
from .views import signup_view, signin_view

app_name = 'accounts'

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("signin/", signin_view, name="signin"),
]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index_view, name='home'),
# ]