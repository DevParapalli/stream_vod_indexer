from django.shortcuts import render
from django.http import JsonResponse

NotImplemented = JsonResponse({"error":"NotImplemented"})
# Create your views here.
def index(request):
    return NotImplemented

def help(request):
    return NotImplemented

def wildcard(request, path):
    return NotImplemented