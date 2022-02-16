from django.shortcuts import render
from .serializers import UsersModelSerializer, TeamsModelSerializer
from rest_framework import viewsets
from .models import Users, Teams
from rest_framework.decorators import action
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


class CustomUsersAPI(viewsets.ViewSet):

    def create(self, request):
        name = request.POST.get('name','')
        if not name:
            return Response({'name': 'Name cannot be Null'})
        email = request.POST.get('email','')
        team_name = request.POST.get('team_name','')
        team_id = Teams.objects.filter(name=team_name).first()
        ph_no = request.POST.get('ph_no','')
        photo = request.FILES['photo']
        user = Users(name=name,
                    email=email,
                    ph_no=ph_no,
                    photo=photo,
                    team_id=team_id)
        user.save()
        serializer = UsersModelSerializer(user)
        return Response(serializer.data)
