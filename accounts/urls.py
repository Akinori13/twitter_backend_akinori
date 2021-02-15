from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('<int:user_id>/followers', views.FollowIndexView.as_view(), name='follow_index'),
    path('<int:user_id>/follow', views.FollowCreateView.as_view(), name='follow_create'),
    path('<int:user_id>/follow/delete', views.FollowDeleteView, name='follow_delete'),
]
