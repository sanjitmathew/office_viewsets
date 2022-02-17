from django.shortcuts import render
from .serializers import UsersModelSerializer, TeamsModelSerializer
from rest_framework import viewsets
from .models import Users, Teams
from rest_framework.decorators import action
from rest_framework.response import Response
import json

IMG_SIZE = 2 * 1024 * 1024

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
        team_ids = data.get('team_ids','')
        if team_ids:
            for id in team_ids:
                team_id = Teams.objects.filter(id=id).first()
                user.team_id.add(team_id)
                user.save()
        serializer = UsersModelSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        global IMG_SIZE
        user = Users.objects.filter(pk=pk).first()
        if user:
            name = request.POST.get('name','')
            if user.name != name:
                user.name = name
            email = request.POST.get('email','')
            if user.email != email:
                user.email = email
            ph_no = request.POST.get('ph_no','')
            if user.ph_no != ph_no:
                if not ph_no.isnumeric():
                    return Response({'ph_no': 'phone no: should be of digits'})
                if len(ph_no) < 10 or len(ph_no) > 15:
                    return Response({'ph_no': 'phone no: should have 10 to 15 digits'})
                user.ph_no = ph_no
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                if photo.size > IMG_SIZE:
                    return Response({'photo': 'Size exceeded 2MB'})
                if not photo.name.endswith(('.jpeg','.png')):
                    return Response({'photo': 'Only jpeg and png allowed'})
                user.photo = photo
            team_ids = request.POST.get('team_ids','')
            if team_ids:
                team_ids = team_ids.split(',')
                team_ids_new = [int(i) for i in team_ids]
                team_ids_obj = user.team_id.all()
                team_ids_old = [i.id for i in team_ids_obj]
                if set(team_ids_old) != set(team_ids_new):
                    for i in team_ids_obj:
                        user.team_id.remove(i)
                    for i in team_ids_new:
                        team = Teams.objects.filter(pk=i).first()
                        if team:
                            user.team_id.add(team)
            user.save()
            serializer = UsersModelSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'msg': 'No such user'})
