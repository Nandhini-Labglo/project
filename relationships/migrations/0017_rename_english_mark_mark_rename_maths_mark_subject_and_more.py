# Generated by Django 4.1.1 on 2022-10-03 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0016_mark_created_by_mark_modified_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='English',
            new_name='mark',
        ),
        migrations.RenameField(
            model_name='mark',
            old_name='Maths',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='Science',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='Social',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='Tamil',
        ),
    ]
