from django.shortcuts import render
from .serializers import UsersModelSerializer, TeamsModelSerializer
from rest_framework import viewsets
from .models import Users, Teams
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# Create your views here.

class UsersAPI(viewsets.ModelViewSet):
    queryset = Users.objects.all().select_related()
    serializer_class = UsersModelSerializer

    @action(detail=True, methods=['get'])
    def active_team_users(self, request, pk=None):
        team = Teams.objects.get(pk=pk)
        if team.is_active:
            users_team = Users.objects.filter(team_id=team)
            serializer = UsersModelSerializer(users_team, many=True)
            return Response(serializer.data)
        else:
            return Response({'msg': 'Inactive team'})
