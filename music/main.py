class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Playing {self.title} by {self.artist}")

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play_all(self):
        for song in self.songs:
            song.play()

# Example usage
song1 = Song("Title 1", "Artist 1", 300)
song2 = Song("Title 2", "Artist 2", 250)
playlist = Playlist("My Playlist")
playlist.add_song(song1)
playlist.add_song(song2)
playlist.play_all()
