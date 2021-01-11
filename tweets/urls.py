from django.urls import path, include
from . import views

app_name = 'tweets'
urlpatterns = [
    path('timeline', views.timeline, name='timeline'),
]