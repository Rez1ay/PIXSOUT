from django.urls import path
from . import views

urlpatterns = [
    path('', views.Forum.as_view(), name='forum'),
    path('<slug:theme_name>', views.theme)
]
