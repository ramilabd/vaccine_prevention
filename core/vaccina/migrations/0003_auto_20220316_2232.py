# Generated by Django 3.2 on 2022-03-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccina', '0002_auto_20220316_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name_department',
            field=models.CharField(max_length=50, verbose_name='Отделение'),
        ),
        migrations.AlterField(
            model_name='groupemployee',
            name='name_grop',
            field=models.CharField(max_length=150, verbose_name='Группа сотрудников'),
        ),
    ]
