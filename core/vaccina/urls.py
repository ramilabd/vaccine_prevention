from django.urls import path
from .views import ViewMainPage, ListEmployee


urlpatterns = [
    path('', ViewMainPage.as_view(), name='index'),
    path('employees', ListEmployee.as_view(), name='employees'),
]