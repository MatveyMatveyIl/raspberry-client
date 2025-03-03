# Generated by Django 4.2.1 on 2023-05-29 15:19

from django.db import migrations, models
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_climateschedule_creation_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_b64', django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True)),
            ],
            options={
                'verbose_name': 'img',
                'verbose_name_plural': 'img',
            },
        ),
    ]
