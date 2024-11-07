from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThemesList.as_view(), name='forum'),
    path('<slug:theme_name>', views.PublicationsList.as_view())
]
