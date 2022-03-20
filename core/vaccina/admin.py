from django.contrib import admin
from .models import (
    GroupEmployee,
    Position,
    Department,
    Employee,
)


@admin.register(GroupEmployee)
class GroupEmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
