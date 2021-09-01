from io import RawIOBase
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from speed.api.serializers import UserDateSerializer
from speed.models import UserData
from speed.api.permissions import IsOwnerData



class UserDataViewSet(viewsets.ModelViewSet):

    queryset = UserData.objects.all()
    lookup_field = "slug"
    serializer_class = UserDateSerializer
    permission_classes = [IsAuthenticated, IsOwnerData]

    def get_queryset(self):
        return UserData.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

