# Generated by Django 4.0.6 on 2022-07-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='icon_background',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
