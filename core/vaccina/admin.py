from distutils import dep_util
from django.contrib import admin
from .models import (
    GroupEmployee,
    Position,
    Department,
    Employee,
)


admin.site.register(GroupEmployee)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Employee)
