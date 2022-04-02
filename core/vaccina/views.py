from django.shortcuts import render, redirect
from django.views import View
from .models import Employee
from .forms import EmployeeForm
from .utils import add_age


class ViewMainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vaccina_page/index.html')


class ListEmployee(View):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        return render(request, 'vaccina_page/employees.html', context={
            'employees': employees,
        })


class ViewEmployeeAdd(View):
    def get(self, request, *args, **kwargs):
        employee_form = EmployeeForm()
        return render(request, 'vaccina_page/add_employee.html', context={
            'form': employee_form,
        })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = EmployeeForm(request.POST)

            if form.is_valid():
                new_form = add_age(form)
                new_form.save()
                return redirect('employees')
