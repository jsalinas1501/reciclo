from rest_framework import serializers
from .models import TrashCan, Level


class TrashCanSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrashCan
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'
        read_only_fields = (
            'time',
        )
