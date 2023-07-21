from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def fun1(request):
    return HttpResponse('this is app1 fun1')

def fun2(request):
    return HttpResponse('this is app2 fun2')
