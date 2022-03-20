from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class GroupEmployee(models.Model):
    name_grop = models.CharField('Группа сотрудников', max_length=150)

    def __str__(self):
        return self.name_grop


class Position(models.Model):
    name_post = models.CharField('Должность', max_length=50)

    def __str__(self):
        return self.name_post


class Department(models.Model):
    name_department = models.CharField('Отделение', max_length=50)

    def __str__(self):
        return self.name_department


class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    date_of_birth = models.DateField('Дата рождения')
    age = models.IntegerField('Возраст')
    post = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.CASCADE)
    group_employee = models.ForeignKey(GroupEmployee,verbose_name='Группа сотрудников', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name='Отделение', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1} {2}, дата рождения: {3}, возраст {4} лет, должность {5}'.format(
            self.first_name,
            self.patronymic,
            self.last_name,
            self.date_of_birth,
            self.age,
            self.post,
        )
