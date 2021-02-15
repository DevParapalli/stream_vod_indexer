from django.urls import path
from server.settings import VERSION
from django.http import HttpResponse
from .views_ import index, help, wildcard
from .views_stream import date, slug, id
from .views_info import slugs, last_updated, streamer, endpoints


# The patterns are tested in order.

urlpatterns = [
    # Stream PATH
    path('stream/date/<int:year>/<int:month>/<int:day>/',date, name="by-date"), # Returns list of streams by date
    path('stream/game/<slug:slug>/', slug, name="by-slug"), # Returns list by game-slug
    path('stream/id/<int:id>/', id, name="by-id"), # Returns Single Object, Use if you know ID
    
    # Info PATH
    path('info/slugs/', slugs, name="get-slugs"), # Returns List of slugs with game names
    path('info/last-updated/', last_updated, name="last-updated"),
    path('info/streamer/', streamer, name="get-streamer-info"),
    path('info/endpoints/', endpoints, name="get-endpoints"),
    path('info/version/', lambda x: HttpResponse(VERSION), name="get-version"),
    
    # Root PATH
    path('', index, name="index"),
    path('help/', help, name="help"),
    path('<path:path>/', wildcard, name="wildcard_url"),
]