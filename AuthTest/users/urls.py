from django.urls import path
from .views import HomeView, ProfileView, MyLoginView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('login/', MyLoginView.as_view(), name="login"),
]