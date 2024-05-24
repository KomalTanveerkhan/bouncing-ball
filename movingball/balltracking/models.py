from django.db import models

# Create your models here.
class MyBall(models.Model):
    x_axis=models.FloatField(max_length=100)
    y_axis=models.FloatField(max_length=100)
    z_axis=models.FloatField(max_length=100)
    ball_bouncing_time=models.DateTimeField()