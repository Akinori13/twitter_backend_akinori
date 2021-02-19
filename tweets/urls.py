from django.urls import path, include
from . import views

app_name = 'tweets'
urlpatterns = [
    # Index(Tweets written by all users)
    path('timeline', views.TimelineView, name='timeline'),
    # Index(Tweets written by a specific user)
    path('<int:user_id>/tweets', views.TweetsView, name='user_tweets'),
    # Read
    path('tweets/<int:pk>', views.TweetDetailView.as_view(), name='detail'),
    # Create
    path('tweets/create', views.TweetCreateView.as_view(), name='create'),
    # Update
    path('tweets/<int:pk>/update', views.TweetUpdateView.as_view(), name='update'),
    # Delete
    path('tweets/<int:pk>/delete', views.TweetDeleteView.as_view(), name='delete'),
    # Like
    path('tweets/<int:pk>/like', views.LikeView, name='like'),
]
