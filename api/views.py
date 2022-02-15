from django.shortcuts import render
from .serializers import UsersModelSerializer, TeamsModelSerializer
from rest_framework import viewsets
from .models import Users, Teams
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# Create your views here.

class UsersAPI(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer

    @action(detail=False, methods=['get'])
    def active_team_users(self, request):
        query_set = Users.objects.filter(team_id__is_active=True)
        serializer = UsersModelSerializer(query_set, many=True)
        return Response(serializer.data)


class TeamsAPI(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsModelSerializer 
