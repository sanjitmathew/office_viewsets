from django.shortcuts import render
from .serializers import UsersModelSerializer, TeamsModelSerializer
from rest_framework import viewsets
from .models import Users, Teams
from rest_framework.decorators import action
from rest_framework.response import Response
import json

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


class CustomUsersAPI(viewsets.ViewSet):

    def create(self, request):
        data = json.loads(request.body)
        name = data.get('name','')
        if not name:
            return Response({'name': 'Name cannot be Null'})
        email = data.get('email','')
        ph_no = data.get('ph_no','')
        if 'photo' in request.FILES:
            photo = request.FILES['photo']
        else:
            photo = None
        user = Users(name=name,
                    email=email,
                    ph_no=ph_no,
                    photo=photo)
        user.save()
        team_names = data.get('team_names','')
        if team_names:
            for team_name in team_names:
                team_id = Teams.objects.filter(name=team_name).first()
                user.team_id.add(team_id)
                user.save()
        serializer = UsersModelSerializer(user)
        return Response(serializer.data)
