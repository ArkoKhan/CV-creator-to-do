# Generated by Django 5.0.1 on 2024-02-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_personalcv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalcv',
            old_name='istitute',
            new_name='institute',
        ),
        migrations.AddField(
            model_name='personalcv',
            name='image',
            field=models.ImageField(default='def.jpg', upload_to='images/'),
        ),
    ]
