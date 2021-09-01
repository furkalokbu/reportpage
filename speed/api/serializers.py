from rest_framework import serializers
from speed.models import UserData
from rest_framework.response import Response

class UserDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        exclude = ["slug", "updated_at"]

