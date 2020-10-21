from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name="inicio"),
    path('home/', HomeView.as_view(), name="home"),

    # path('register/', RegisterView.as_view(), name="register")
]
