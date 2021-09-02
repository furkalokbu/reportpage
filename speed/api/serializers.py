from django.db.models import fields
from rest_framework import serializers
from speed.models import UserData
from rest_framework.response import Response
from speed.models import SpeedUserData

class UserDateSerializer(serializers.ModelSerializer):

    average_speed = serializers.SerializerMethodField()

    class Meta:
        model = UserData
        exclude = ["slug", "updated_at"]

    def get_average_speed(self, obj):
        request = self.context.get("request")
        query = SpeedUserData.objects.filter(user=request.user).first()
        if query:
            return query.average_speed
        else:
            return 0


class ReportUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserData
        fields = ['date', 'distance', 'duration']

