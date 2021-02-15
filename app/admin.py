from django.contrib import admin
from .models import GameStorage, StreamStorage

# Register your models here.
class GameStorageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'game_slug': ('game_name',), }
    
admin.site.register(GameStorage, GameStorageAdmin)

class StreamStorageAdmin(admin.ModelAdmin):
    pass

admin.site.register(StreamStorage, StreamStorageAdmin)