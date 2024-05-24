# Generated by Django 5.0.6 on 2024-05-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_axis', models.FloatField(max_length=100)),
                ('y_axis', models.FloatField(max_length=100)),
                ('z_axis', models.FloatField(max_length=100)),
                ('ball_bouncing_time', models.DateTimeField()),
            ],
        ),
    ]
