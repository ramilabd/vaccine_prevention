# Generated by Django 3.2 on 2022-03-26 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccina', '0003_auto_20220316_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='date_of_birth',
            new_name='birthday',
        ),
    ]
