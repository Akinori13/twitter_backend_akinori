from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import CustomUserCreationForm
from .models import User
from django.views import generic

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

