from __future__ import annotations

# Define a class 'Song'
class Song:
    def __init__(self, name: str, artist: str, genre: str, duration: str):
        self.song_name = name
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.set_duration(duration)  # Call the function song.set_duration in __init__


    def get_name(self) -> str:
        return self.song_name
    
    def get_artist(self) -> str:
        return self.artist

    def get_genre(self) -> str:
        return self.genre

    def set_duration(self, duration: str) -> None:
        self.duration = duration
        mm_ss = self.duration.split(':')  # Split the string MM:SS into minute and second parts
        minutes = int(mm_ss[0])
        seconds = int(mm_ss[1])

        total_sec = minutes * 60 + seconds
        self.duration = total_sec
        return 


    def get_duration(self) -> int:
        return self.duration

    def is_same(self, check_song: Song) -> bool:
        # Use logic Truth to return the boolen value of this function
        return self.song_name == check_song.song_name and self.artist == check_song.artist

    def has_same_artist(self, check_song: Song) -> bool:
        return self.artist == check_song.artist
        
    def has_same_genre(self, check_song: Song) -> bool:
        return self.genre == check_song.genre

    def get_longest(self, check_song: Song) -> Song | None:
        # '-> Song | None' means return an object or None, if they're same length
        if self.get_duration() > check_song.get_duration():
            return self  # Self is an object
        elif self.get_duration() < check_song.get_duration():
            return check_song  # check_song is also an object
        else:
            return
        
    def __str__(self):
        return f"{self.song_name} by {self.artist} ({self.genre}, {self.duration}s)"

        
if __name__ == '__main__':
    pass