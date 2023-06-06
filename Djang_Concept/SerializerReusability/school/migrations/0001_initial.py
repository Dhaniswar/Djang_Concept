# Generated by Django 3.2 on 2022-09-29 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=254)),
                ('marks', models.IntegerField()),
                ('pass_date', models.DateTimeField()),
            ],
        ),
    ]
