# Generated by Django 2.2.5 on 2019-12-02 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('local_code', models.IntegerField()),
                ('cold_index', models.IntegerField()),
                ('asthma_index', models.IntegerField()),
                ('stroke_index', models.IntegerField()),
            ],
        ),
    ]
