from django.db import models



# Create your models here.
class GameStorage(models.Model):
    game_name = models.CharField(max_length=200)
    game_slug = models.CharField(max_length=200)
    game_steam_id = models.IntegerField(default=-1)
    

class StreamStorage(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    date_of_stream = models.DateField()
    stream_title = models.CharField(max_length=200)
    game = models.ForeignKey(GameStorage, on_delete=models.RESTRICT)
    