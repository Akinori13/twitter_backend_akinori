from django.urls import path, include
from . import views

app_name = 'tweets'
urlpatterns = [
    # Index
    path('timeline', views.TimelineView.as_view(), name='timeline'),
    # Read
    path('<int:pk>', views.TweetDetailView.as_view(), name='detail'),
    # Create
    path('create', views.TweetCreateView.as_view(), name='create'),
    # Update
    path('<int:pk>/update', views.TweetUpdateView.as_view(), name='update'),
    # Delete
    path('<int:pk>/delete', views.TweetDeleteView.as_view(), name='delete'),
]
