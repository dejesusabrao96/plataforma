from .models import Activities
from rest_framework import serializers

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = "__all__"

    