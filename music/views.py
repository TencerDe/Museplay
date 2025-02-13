from django.shortcuts import render, get_object_or_404
from .models import Song

# Create your views here.

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'music/play_song.html', {'song': song})