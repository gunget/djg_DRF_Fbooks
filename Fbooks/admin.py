from django.contrib import admin
# from .models import Fbooks
from .models import Fbooks, Users

# admin.site.register(Fbooks)
admin.site.register([Fbooks, Users])

# Register your models here.
