# Generated by Django 4.2.7 on 2023-11-21 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_alter_project_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee_project',
            table='employee_project',
        ),
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
    ]
