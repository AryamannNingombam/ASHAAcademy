# Generated by Django 3.1.7 on 2021-04-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashaAPI', '0014_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]