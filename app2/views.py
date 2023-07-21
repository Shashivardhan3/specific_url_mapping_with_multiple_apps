from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def shashi(request):
    return HttpResponse ('shashi vardhan')


def vardhan(request):
    return HttpResponse('kurnool')