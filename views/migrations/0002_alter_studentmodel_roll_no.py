# Generated by Django 4.1.1 on 2022-09-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='Roll_no',
            field=models.IntegerField(null=True),
        ),
    ]
