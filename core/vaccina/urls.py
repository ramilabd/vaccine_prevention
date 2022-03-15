from django.urls import path
from .views import ViewMainPage


urlpatterns = [
    path('', ViewMainPage.as_view(), name='index'),
]