from app2.views import *

from django.urls import path

app_name='shashi'


urlpatterns = [
    path('shashi/',shashi,name='shashi'),
    path('vardhan/',vardhan,name='vardhan')
]
