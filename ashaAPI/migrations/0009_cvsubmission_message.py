# Generated by Django 3.1.7 on 2021-03-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashaAPI', '0008_delete_teacherimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvsubmission',
            name='message',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]