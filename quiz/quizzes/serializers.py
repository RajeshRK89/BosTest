
from rest_framework import serializers
from .models import *

class quizserializer(serializers.ModelSerializer):
    
    class Meta:
        model = response
        fields = '__all__'