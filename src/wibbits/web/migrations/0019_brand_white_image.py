# Generated by Django 4.0.6 on 2022-07-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='white_image',
            field=models.FileField(blank=True, null=True, upload_to='brands/'),
        ),
    ]