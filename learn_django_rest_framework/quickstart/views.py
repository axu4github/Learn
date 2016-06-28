from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.generics import CreateAPIView
from quickstart.serializers import UserSerializer, GroupSerializer, QuerySerializer
from models import Query


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'query': reverse('query', request=request, format=format),
        'query4view': reverse('query4view', request=request, format=format),
        'query4mixinview': reverse('query4mixinview', request=request, format=format),
    })


@api_view(['GET'])
def query(request, format=None):
    '''
        url => http://127.0.0.1:8000/query/?context=%27select%20*%20from%20a%27
    '''
    requestData = {'context': 'select * from a'}
    serializer = QuerySerializer(data=requestData)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QueryView(APIView):

    def post(self, request, format=None):
        requestData = {'context': request.data}
        print request.data
        serializer = QuerySerializer(data=requestData)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QueryMixinView(CreateAPIView):
    """docstring for QueryMixinView"""

    serializer_class = QuerySerializer

    def post(self, request):
        print request.data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QueryViewSet(viewsets.ModelViewSet):
    """docstring for QueryViewSet"""

    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    


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
