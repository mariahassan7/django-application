# Generated by Django 4.2.4 on 2023-08-29 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data', '0008_alter_employee_upload_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='upload_image',
        ),
    ]