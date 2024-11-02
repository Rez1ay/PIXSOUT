from django.urls import path
from . import views

urlpatterns = [
    path('', views.Donate.as_view(), name='donate')
]
