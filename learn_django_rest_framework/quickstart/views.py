from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from quickstart.serializers import UserSerializer, GroupSerializer, QuerySerializer
from django.http import JsonResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def query(request):
    responseData = {'sql': '123123123'}
    serializer = QuerySerializer(data=responseData)
    if serializer.is_valid():
        return JsonResponse(serializer.data)

    return JsonResponse(serializer.errors, status=400)
