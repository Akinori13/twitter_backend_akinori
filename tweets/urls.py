from django.urls import path, include
from . import views

app_name = 'tweets'
urlpatterns = [
    # Read
    path('timeline', views.timeline, name='timeline'),
    # Create
    path('create', views.create, name='create'),
    # Update
    path('edit', views.edit, name='edit'),
    # Delete
    path('delete', views.delete, name='delete'),
]
