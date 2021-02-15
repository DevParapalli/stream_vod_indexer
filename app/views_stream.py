from django.shortcuts import render
import datetime
from django.core.serializers import serialize
from app.models import GameStorage, StreamStorage
from django.http import JsonResponse

NotImplemented = JsonResponse({"error": "NotImplemented"})


def __is_date_valid(year: int, month: int, day: int):
    try:
        datetime.datetime(year=year, month=month, day=day)
        return True
    except ValueError:
        return False


def date(request, year: int, month: int, day: int):
    return JsonResponse(
        {
            'data': [obj for obj in StreamStorage.objects.filter(
                date_of_stream__year=year,
                date_of_stream__month=month,
                date_of_stream__day=day,
                vod_status=True
            ).values()]
        }
    )


def slug(request, slug: str):

    return JsonResponse(
        {
            'data': [obj for obj in StreamStorage.objects.filter(
                game__game_slug__iexact=slug,
                vod_status=True
            ).values()]
        }
    )


def id(request, id: int):
    return JsonResponse(
        {
            'data': StreamStorage.objects.filter(id=id).values()[0]
        }
    )
