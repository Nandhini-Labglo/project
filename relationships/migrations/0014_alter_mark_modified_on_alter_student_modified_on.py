# Generated by Django 4.1.1 on 2022-10-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0013_mark_modified_on_student_modified_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
