from django.urls import path
from .views import ViewMainPage, ListEmployee, ViewEmployeeAdd


urlpatterns = [
    path('', ViewMainPage.as_view(), name='index'),
    path('employees', ListEmployee.as_view(), name='employees'),
    path('add_employee', ViewEmployeeAdd.as_view(), name='form_add_employee')
]