# Generated by Django 3.1.7 on 2021-03-18 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ashaAPI', '0006_auto_20210317_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='teachercard',
            name='teacherImage',
            field=models.ImageField(upload_to='TeacherImages/'),
        ),
        migrations.AlterField(
            model_name='teachercard',
            name='facultySubject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ashaAPI.subject'),
        ),
    ]
