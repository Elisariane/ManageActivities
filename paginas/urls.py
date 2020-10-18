from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name="inicio"),
    path('home/', HomeView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register")
]
