from django.urls import path
from .views import song_list, play_song, user_signup, user_login, user_logout

urlpatterns = [
    path('', song_list, name='song_list'),  # Homepage: Show list of songs
    path('play/<int:song_id>/', play_song, name='play_song'),  # Play song
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
