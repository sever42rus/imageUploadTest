from django.urls import path
from . import views

app_name = 'image'
urlpatterns = [
    path('list/', views.ImageListAPI.as_view()),
    path('create/', views.ImageCreateAPI.as_view()),
]
