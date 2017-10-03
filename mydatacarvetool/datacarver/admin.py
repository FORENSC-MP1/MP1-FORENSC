from django.contrib import admin

# Register your models here.
from . models import Filesig
from . models import information

admin.site.register(Filesig)
admin.site.register(information)