from django.db import models



# Create your models here.
class GameStorage(models.Model):
    game_name = models.CharField(max_length=200)
    game_slug = models.SlugField(max_length=200)
    game_steam_id = models.IntegerField(default=-1)
    game_webpage_link = models.URLField(blank=True, max_length=1000)

    def __str__(self):
        return self.game_slug
class StreamStorage(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    date_of_stream = models.DateField()
    stream_title = models.CharField(max_length=200)
    game = models.ForeignKey(GameStorage, on_delete=models.RESTRICT)
    vod_link = models.URLField(blank=True, max_length=1000)
    vod_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.game}-{self.date_of_stream}"