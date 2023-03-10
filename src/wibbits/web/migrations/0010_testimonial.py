# Generated by Django 4.0.6 on 2022-07-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_video_play_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonial/')),
                ('logo', models.FileField(blank=True, null=True, upload_to='testimonial/')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=256)),
                ('designation', models.CharField(max_length=256)),
                ('company_name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'web_testimonial',
                'ordering': ['-id'],
            },
        ),
    ]
