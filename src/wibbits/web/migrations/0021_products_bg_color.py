# Generated by Django 4.0.6 on 2022-07-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_products_hero_image_products_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='bg_color',
            field=models.CharField(default='#ffc9b7', max_length=256),
            preserve_default=False,
        ),
    ]
