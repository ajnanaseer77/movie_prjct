# Generated by Django 3.2.23 on 2024-01-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]