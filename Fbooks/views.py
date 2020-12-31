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

from django.views.generic import View
from django.http import HttpResponse
# from django.conf import settings
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# 현재 파일의 부모경로를 sys.path에 추가해줌. 이러면 부모 경로와 동등 똫는 하위의 파일들을 불러쓸 수 있게 됨 
from RctDjgPJT import settings

# raw string이용
# BASE_DIR = (r'D:\김건\개인자료\python 수업\RctDjgPJT\RctDjgPJT')
# D:\김건\개인자료\JavaScript_PJT\Nomad\rct_hooks_phonebook\build

class ReactAppView(View):

    def get(self, request):
        try:
            # with open('D:\\김건\\개인자료\\JavaScript_PJT\\Nomad\\rct_hooks_phonebook\\build\\index.html') as file:
            with open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(settings.BASE_DIR))),'JavaScript_PJT', 'Nomad', 'rct_hooks_phonebook', 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except:
            return HttpResponse(status=501,)

# Create your views here.
