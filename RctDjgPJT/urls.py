"""RctDjgPJT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from Fbooks import views

route = routers.DefaultRouter()
route.register('fbooks', views.FbooksView, 'Fbooks')
route.register('users', views.UserView, 'users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path("", views.ReactAppView.as_view()),
    path("rest-auth/", include('rest_auth.urls')),
    path("rest-auth/registration/", include('rest_auth.registration.urls')),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API EndPoint
# << Basic >>
# /rest-auth/login/ (POST)
# username
# email
# password
# Returns Token key

# /rest-auth/logout/ (POST)

# /rest-auth/password/reset/ (POST)
# email

# /rest-auth/password/reset/confirm/ (POST)
# uid
# token
# new_password1
# new_password2

# /rest-auth/password/change/ (POST)
# new_password1
# new_password2
# old_password

# /rest-auth/user/ (GET, PUT, PATCH)
# username
# first_name
# last_name
# Returns pk, username, email, first_name, last_name

# << Registration >>
# /rest-auth/registration/ (POST)
# username
# password1
# password2
# email

# /rest-auth/registration/verify-email/ (POST)
# key