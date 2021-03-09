from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', views.LogoutAPI.as_view(), name='logout'),
    path('login-as/<int:user>/',
         staff_member_required(views.login_as), name="login_as"),
]
