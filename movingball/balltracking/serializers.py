from .models import MyBall
from rest_framework import serializers

class MyBallSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyBall
        fields='__all__'
        
    