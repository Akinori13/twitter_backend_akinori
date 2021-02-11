from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tweet
from accounts.models import User


# Create your views here.
class TimelineView(LoginRequiredMixin, ListView):
    queryset = Tweet.objects.order_by('-created_at')
    paginate_by = 4
    template_name = 'tweets/timeline.html'
    context_object_name = 'tweets'


class TweetDetailView(LoginRequiredMixin, DetailView):
    model = Tweet
    template_name = 'tweets/detail.html'
    context_object_name = 'tweet'


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    fields = ['text']
    template_name = 'tweets/create.html'
    success_url = reverse_lazy('tweets:timeline')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin, UpdateView):
    model = Tweet
    fields = ['text']
    template_name = 'tweets/update.html'
    success_url = reverse_lazy('tweets:timeline')


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweets:timeline')

def TweetsView(request, user_id):
    queryset1 = Tweet.objects.filter(user__id=user_id)
    queryset2 = User.objects.get(pk=user_id)
    context = {'tweets':queryset1,'user':queryset2}
    return render(request, 'tweets/index.html', context)
