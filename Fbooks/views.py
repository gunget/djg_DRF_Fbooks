from django.shortcuts import render
from rest_framework import viewsets
# from .serializers import FbooksSerializer
from .serializers import FbooksSerializer, UserSerializer
# from .models import Fbooks
from .models import Fbooks, Users

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class FbooksView(viewsets.ModelViewSet):
    queryset = Fbooks.objects.all()
    serializer_class = FbooksSerializer

# os.path.join(os.path.dirname(BASE_DIR), 'javascript', 'react', 'rct_hooks_phonebooks', 'build')

class ReactAppView(View):

    def get(self, request):
        try:
            with open('D:\\개인자료\\김건\\javascript\\react\\rct_hooks_phonebooks\\build\\index.html') as file:
            # with open(os.path.join(os.path.dirname(BASE_DIR), 'javascript', 'react', 'rct_hooks_phonebooks', 'build', 'index.html')) as file:
            # with open(os.path.join(str(settings.ROOT_DIR),
            #                         'front',
            #                         'build',
            #                         'index.html')) as file:
                return HttpResponse(file.read())

        except:
            return HttpResponse(status=501,)

# Create your views here.
