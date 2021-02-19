from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db import IntegrityError

from .models import Tweet, Like
from accounts.models import User


# Create your views here.
@login_required
def TimelineView(request):
    tweets = Tweet.objects.order_by('-created_at')
    liked_list = request.user.like_set.values_list('tweet', flat=True)
    context = {'liked_list':liked_list, 'tweets':tweets}
    return render(request, 'tweets/timeline.html', context)


class TweetDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tweet
    template_name = 'tweets/detail.html'
    context_object_name = 'tweet'


class TweetCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tweet
    fields = ['text']
    template_name = 'tweets/create.html'
    success_url = reverse_lazy('tweets:timeline')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tweet
    fields = ['text']
    template_name = 'tweets/update.html'
    success_url = reverse_lazy('tweets:timeline')


class TweetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweets:timeline')

@login_required
def TweetsView(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    tweets = user.tweet_set.all()
    context = {'user':user, 'tweets':tweets}
    
    return render(request, 'tweets/index.html', context)

@login_required
@require_POST
def LikeView(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    like = Like.objects.filter(user=request.user, tweet=tweet)
    if like:
        like.delete()
    else:
        like.create(user=request.user, tweet=tweet)

    return JsonResponse({'likes_num': tweet.like_set.count()})
