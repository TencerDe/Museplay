from django.shortcuts import render, get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from .models import Song
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'music/play_song.html', {'song': song})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'music/signup.html', {'form':form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('song_list')  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'music/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
