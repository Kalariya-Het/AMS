# Generated by Django 3.0.7 on 2024-08-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_auto_20240828_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.FileField(upload_to=''),
        ),
    ]
