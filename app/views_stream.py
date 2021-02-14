from django.shortcuts import render
import datetime
from django.http import JsonResponse

NotImplemented = JsonResponse({"error": "NotImplemented"})


def __is_date_valid(year: int, month: int, day: int):
    try:
        datetime.datetime(year=year, month=month, day=day)
        return True
    except ValueError:
        return False


def date(request, year: int, month: int, day: int):
    return NotImplemented


def slug(request, slug: str):
    return NotImplemented


def id(request, id: int):
    return NotImplemented
