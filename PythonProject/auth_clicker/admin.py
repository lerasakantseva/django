from .models import UserData
from django.contrib import admin
from .models import Note

admin.site.register(Note)
admin.site.register(UserData)