# Generated by Django 3.1.7 on 2021-03-06 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ashaAPI', '0003_auto_20210306_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachercard',
            old_name='isInManagements',
            new_name='isInManagement',
        ),
    ]
