# class Playlist:
#     def __init__(self,name ):
#         self.name=name
#         self.songs=[]

#     def add_song(self,song):
#         self.songs.append(song)
#         print(f"Added: {song}")

#     def remove_song(self, song):
#         if song in self.songs:
#             self.song.remove(song)
#             print(f"Removed: {song}")

#     def show_songs(self):
#         print(f"Playliust '{self.name}' :")
#         for song in self.songs:
#             print(f" -{song}")

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.show_songs()         


class song:
    def __init__(self,title,artist,album,duration):
        self.title=title
        self.artist=artist
        self.album=album
        self.duration=duration
    def __str__(self):
        return f"{self.song} {self.name}{self.title}{self.artist}{self.alubum}{self.duration}"

class Playlist:
  
    def __init__(self,name ):
        self.name=name
        self.songs=[]

    def __str__(self):
        return f"{self.song} {self.name}{self.title}{self.artist}{self.alubum}{self.duration}" 
    

    def add_song(self,song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.song.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playliust '{self.name}' :")
        for song in self.songs:
            print(f" -{song}")


song1=song("shape of you","ed sheeran","divide",240)
song2=song("shape of you","ed sheeran","divide",240)

my_playlist = Playlist("Niki")
my_playlist.add_song(song1.song)
my_playlist.add_song(song2)
my_playlist.show_songs()          