# Generated by Django 3.1.7 on 2021-03-30 13:59

from django.db import migrations, models
import django.db.models.deletion
import student_portal.models


class Migration(migrations.Migration):

    dependencies = [
        ('ashaAPI', '0012_delete_teachercard'),
        ('student_portal', '0005_marksheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('classFor', models.IntegerField()),
                ('paperPDF', models.FileField(upload_to=student_portal.models.uploadToCallbackQuestionPaper)),
                ('subjectFor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashaAPI.subject')),
            ],
        ),
        migrations.AddField(
            model_name='marksheet',
            name='questionPaper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_portal.questionpaper'),
        ),
    ]