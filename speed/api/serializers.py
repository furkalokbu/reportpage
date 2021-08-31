from rest_framework import serializers
from speed.models import UserData
from rest_framework.response import Response

class UserDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        exclude = ["slug", "updated_at"]

    def get_average_speed(self,instance):
        request = self.context.get("request")
        return instance.userdata.filter(user=request.user).exists()
        
    def get(self, request):
        return Response(
            { "average_speed": 10}
        )