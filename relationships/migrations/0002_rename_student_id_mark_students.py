# Generated by Django 4.1.1 on 2022-09-24 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='student_ID',
            new_name='students',
        ),
    ]