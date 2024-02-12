# Generated by Django 5.0.1 on 2024-02-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=20)),
                ('task_date', models.DateField()),
                ('task_time', models.TimeField()),
            ],
        ),
    ]
