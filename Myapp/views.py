from django.shortcuts import render
from .models import Data
from .serializers import DataSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

def home(request):
    if request.method =='POST':
        title=request.POST['title']
        author=request.POST['author']
        publisher=request.POST['publisher']
        obj=Data()
        obj.title=title
        obj.author=author
        obj.publisher=publisher
        obj.save()
    return render(request,'home.html')

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'CREATE':'',
        'READ':'/read/',
        'DETAIL':'/detail/<str:pk>/',
        'UPDATE':'/update/<str:pk>',
        'DELETE':'/delete/<str:pk>',
        'AUTHORIZED USER':'/user/',
        'GET TOKEN':'/api/token',
        'REFRESH TOKEN':'/api/token/refresh/',
    }
    return Response(api_urls)


@api_view(['GET'])
def read(request):
    queryset = Data.objects.all()
    serializer = DataSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def details(request, pk):
    
    instance = get_object_or_404(Data, pk=pk)
    serializer = DataSerializer(instance)
    return Response(serializer.data)

@api_view(['POST'])
def update(request,pk):
    task = get_object_or_404(Data, pk=pk)
    serializer=DataSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request,pk):
    task = get_object_or_404(Data, pk=pk)
    task.delete()
    return Response("Item successfully deleted")



class User(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Data.objects.all()
        serializer = DataSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)