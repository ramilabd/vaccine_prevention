from django.forms import ModelForm, TextInput, DateInput, HiddenInput
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Имя',

            }),
            'patronymic': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Отчество',

            }),
            'last_name': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Фамилия',

            }),
            'birthday': DateInput(attrs={
                'class': 'forms',
                'placeholder': 'Дата рождения',
            }),
            'age': HiddenInput(attrs={
                'class': 'forms'
            })
        }