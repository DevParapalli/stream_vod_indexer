from django.contrib import admin
from .models import GameStorage, StreamStorage

# Register your models here.
admin.site.register(GameStorage)
admin.site.register(StreamStorage)