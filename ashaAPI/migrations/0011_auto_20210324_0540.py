# Generated by Django 3.1.7 on 2021-03-24 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ashaAPI', '0010_cvsubmission_subjectapplyingfor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvsubmission',
            name='subjectApplyingFor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ashaAPI.subject'),
        ),
    ]