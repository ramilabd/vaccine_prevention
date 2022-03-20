from django.shortcuts import render
from django.views import View
from .models import Employee


class ViewMainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vaccina_page/index.html')


class ListEmployee(View):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        return render(request, 'vaccina_page/employees.html', context={
            'employees': employees,
        })
