# Generated by Django 3.1.7 on 2021-03-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0003_auto_20210326_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='isStudent',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='isTeacher',
            field=models.BooleanField(default=False, null=True),
        ),
    ]