# Generated by Django 4.1.1 on 2022-10-03 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0018_alter_mark_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='modified_by',
        ),
    ]