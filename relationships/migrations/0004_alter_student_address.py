# Generated by Django 4.1.1 on 2022-09-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0003_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Address',
            field=models.TextField(null=True),
        ),
    ]
