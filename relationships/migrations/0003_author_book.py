# Generated by Django 4.1.1 on 2022-09-24 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0002_rename_student_id_mark_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=30, null=True)),
                ('authors', models.ManyToManyField(to='relationships.author')),
            ],
        ),
    ]
