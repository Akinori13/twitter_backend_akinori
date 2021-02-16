from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import User, Connect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweets:timeline')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

class FollowIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'accounts/follow/index.html'
    context_object_name = 'followers'

    def get_queryset(self):
        return Connect.objects.filter(followed_user__id=self.kwargs['user_id']).select_related('user')

class FollowCreateView(LoginRequiredMixin, generic.CreateView):
    model = Connect
    fields = []
    template_name = 'accounts/follow/create.html'

    def get_success_url(self):
        return reverse('tweets:user_tweets', args=[self.kwargs['user_id']])

    def form_valid(self, form):
        form.instance.user = User.objects.get(pk=self.request.user.id)
        form.instance.followed_user = get_object_or_404(User, pk=self.kwargs['user_id'])

        if form.instance.user == form.instance.followed_user:
            form.add_error(None, "You cannot follow yourself.")
            return super().form_invalid(form)
        elif Connect.objects.filter(user=form.instance.user, followed_user=form.instance.followed_user).exists():
            form.add_error(None, "You've already followed this account.")
            return super().form_invalid(form)
        
        return super().form_valid(form)

@login_required
def FollowDeleteView(request, user_id):
    user = User.objects.get(pk=request.user.id)
    try:
        followed_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("This user does not exist.")

    connect = Connect.objects.filter(
            user=user, 
            followed_user=followed_user
    )

    connect.delete()

    return HttpResponseRedirect(
        reverse(
            'tweets:user_tweets',
            args=[user_id]
        )
    )
