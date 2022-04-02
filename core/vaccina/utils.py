from xmlrpc.client import DateTime


from datetime import datetime
from .forms import EmployeeForm


def add_age(form) -> EmployeeForm:
    today = datetime.today()
    birthday = form.cleaned_data['birthday']

    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day < birthday.day:
        age -= 1

    data = form.cleaned_data
    data['age'] = age

    return EmployeeForm(data)
