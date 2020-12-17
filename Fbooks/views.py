from django.shortcuts import render
from rest_framework import viewsets
# from .serializers import FbooksSerializer
from .serializers import FbooksSerializer, UserSerializer
# from .models import Fbooks
from .models import Fbooks, Users

class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class FbooksView(viewsets.ModelViewSet):
    queryset = Fbooks.objects.all()
    serializer_class = FbooksSerializer

# Create your views here.
