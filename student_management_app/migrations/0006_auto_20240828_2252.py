# Generated by Django 3.0.7 on 2024-08-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
