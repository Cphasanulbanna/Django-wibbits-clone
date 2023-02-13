# Generated by Django 4.0.6 on 2022-07-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_marketingfeature_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='products/')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
            ],
            options={
                'db_table': 'web_products',
                'ordering': ['-id'],
            },
        ),
    ]
