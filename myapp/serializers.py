from rest_framework import serializers
from myapp.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username', 'password')