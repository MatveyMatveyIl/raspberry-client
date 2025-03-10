# Generated by Django 4.2 on 2023-05-06 13:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_humidity_hydrogenindicator_illumination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Climate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(choices=[('Нагрев', 'Heat'), ('Проветривание', 'Ventilation')], verbose_name='тип работы')),
            ],
            options={
                'verbose_name': 'Ручной микроклимат',
                'verbose_name_plural': 'Ручной микроклимат',
            },
        ),
        migrations.CreateModel(
            name='ClimateSchedule',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('t_max', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Максимальная температура')),
                ('t_necessary', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Необходимая температура')),
                ('t_min', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Минимальная температура')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('taken', models.BooleanField(default=False, verbose_name='расписание зафиксировано')),
            ],
            options={
                'verbose_name': 'Расписание микроклимата',
                'verbose_name_plural': 'Расписание микроклимата',
            },
        ),
        migrations.CreateModel(
            name='ClimateState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('авто', 'Auto'), ('ручной', 'Manual'), ('выключено', 'Off')], verbose_name='тип работы')),
            ],
            options={
                'verbose_name': 'Состояние микроклимата',
                'verbose_name_plural': 'Состояние микроклимата',
            },
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_channel', models.IntegerField(verbose_name='красный канал')),
                ('G_channel', models.IntegerField(verbose_name='зеленый канал')),
                ('B_channel', models.IntegerField(verbose_name='синий канал')),
                ('brightness', models.IntegerField(verbose_name='яркость')),
            ],
            options={
                'verbose_name': 'Ручное освещение',
                'verbose_name_plural': 'Ручное освещение',
            },
        ),
        migrations.CreateModel(
            name='LightSchedule',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('R_channel', models.IntegerField(verbose_name='красный канал')),
                ('G_channel', models.IntegerField(verbose_name='зеленый канал')),
                ('B_channel', models.IntegerField(verbose_name='синий канал')),
                ('brightness', models.IntegerField(verbose_name='яркость')),
                ('time_start', models.CharField(verbose_name='начало расписания')),
                ('time_end', models.CharField(verbose_name='конец расписания')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('taken', models.BooleanField(default=False, verbose_name='расписание зафиксировано')),
            ],
            options={
                'verbose_name': 'Расписание освещения',
                'verbose_name_plural': 'Расписание освещения',
            },
        ),
        migrations.CreateModel(
            name='LightState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('авто', 'Auto'), ('ручной', 'Manual'), ('выключено', 'Off')], verbose_name='тип работы')),
            ],
            options={
                'verbose_name': 'Состояние освещения',
                'verbose_name_plural': 'Состояние освещения',
            },
        ),
        migrations.AlterModelOptions(
            name='humidity',
            options={'verbose_name': 'Влажность', 'verbose_name_plural': 'Влажность'},
        ),
        migrations.AlterModelOptions(
            name='hydrogenindicator',
            options={'verbose_name': 'pH', 'verbose_name_plural': 'pH'},
        ),
        migrations.AlterModelOptions(
            name='illumination',
            options={'verbose_name': 'Освещение', 'verbose_name_plural': 'Освещение'},
        ),
        migrations.AlterModelOptions(
            name='solutionconductivity',
            options={'verbose_name': 'Проводимость раствора', 'verbose_name_plural': 'Проводимость раствора'},
        ),
        migrations.AlterModelOptions(
            name='temperature',
            options={'verbose_name': 'Температура', 'verbose_name_plural': 'Температура'},
        ),
    ]
