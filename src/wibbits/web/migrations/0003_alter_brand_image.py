# Generated by Django 4.0.6 on 2022-07-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.FileField(upload_to='brands/'),
        ),
    ]