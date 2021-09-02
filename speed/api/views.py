from io import RawIOBase
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from speed.api.serializers import UserDateSerializer, ReportUserSerializer
from speed.models import UserData
from speed.api.permissions import IsOwnerData
from django.db.models.functions import Cast, TruncDay, TruncMonth, TruncWeek, TruncYear, TruncDate, Extract
from django.db.models import  Avg, Sum, DateField
from rest_framework.response import Response
from rest_framework import status


class UserDataViewSet(viewsets.ModelViewSet):

    queryset = UserData.objects.all()
    lookup_field = "slug"
    serializer_class = UserDateSerializer
    permission_classes = [IsAuthenticated, IsOwnerData]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return UserData.objects.filter(user=self.request.user)


class ReportUserViewSet(viewsets.ModelViewSet):

    serializer_class = ReportUserSerializer
    queryset = UserData.objects.all()   
    http_method_names = ['get', 'post', 'head']

    GROUP_CASTING_MAP = { 
        'day': Cast(TruncDay('date'), output_field=DateField()),
        'month': Cast(TruncMonth('date'), output_field=DateField),
        'week': Cast(TruncWeek('date'), output_field=DateField()),
        'year': Cast(TruncYear('date'), output_field=DateField()),
    }
    
    GROUP_ANNOTATIONS_MAP = {  # Defines the fields used for grouping
        'day': {
            'day': TruncDay('date'),
            'month': TruncMonth('date'),
            'year': TruncYear('date'),
        },
        'week': {
            'week': TruncWeek('date')
        },
        'month': {
            'month': TruncMonth('date'),
            'year': TruncYear('date'),
        },
        'year': {
            'year': TruncYear('date'),
        },
    }

    def get_queryset(self):
        return UserData.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        
        group_by_field = request.GET.get('group_by', None)
        if group_by_field and group_by_field not in self.GROUP_CASTING_MAP.keys():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        queryset = self.filter_queryset(self.get_queryset())

        if group_by_field:
            
            queryset = queryset.annotate(**self.GROUP_ANNOTATIONS_MAP[group_by_field]) \
                .values(*self.GROUP_ANNOTATIONS_MAP[group_by_field]) \
                .annotate(distance=Sum('distance'), duration=Sum('duration'), date=self.GROUP_CASTING_MAP[group_by_field]) \
                .values('duration', 'distance','date')
            
            print(queryset)
        
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)