class Pop_Songs:
    def __init__(self, TitleSong, ReleaseYear, LengthSongInSeconds, SingerSong):
        self.title = TitleSong
        self.__release_year = ReleaseYear
        self.__length_of_song = LengthSongInSeconds
        self.singer = SingerSong

    def ReturnTitle(self):
       print(f"The title of the song is {self.title}")
    def ChangeSinger(self, NewSinger ):
        self.singer = NewSinger
    def loopsong(self, NumberOfLoops):
       print(f"The song will be looped for this many times: {NumberOfLoops}")
       
class Song_Compiler:
    def __init__(self, GenreSong):
        self.Genre = GenreSong
        self.compiled_songs = []

    def add_Songs(self, songs):
        self.compiled_songs.append(songs)

Song1 = Pop_Songs("Kid and Leveret", 2024, 180, "Yaelokre")

Song2 = Pop_Songs("From Now On", 2023, 182, "Hugh Jackman")

Song3 = Pop_Songs("Torete", 2018, 172, "Yeng Constantino")

SongCompiler1 = Song_Compiler("Pop")

print("---BEFORE RELATIONSHIP---")
print(f"Song 1: {Song1.title}, {Song1.singer}")
print(f"Song 2: {Song2.title}, {Song2.singer}")
print(f"Song 3: {Song3.title}, {Song3.singer}")
print(f"Song Compiler 1: {SongCompiler1.compiled_songs}")

SongCompiler1.add_Songs(Song1)
SongCompiler1.add_Songs(Song2)
SongCompiler1.add_Songs(Song3)

print("")
print("---BUILDING RELATIONSHIP---")
print("Song 1,2, and 3 are being associated in SongCompiler1.")

print("")
print("---AFTER RELATIONSHIP---")
print("Title of songs stored in SongCompiler1: ")
for Song_Compiler in SongCompiler1.compiled_songs:
    print(Song_Compiler.title)

print("")
print("Singer of songs stored in SongCompiler1: ")
for Song_Compiler in SongCompiler1.compiled_songs:
    print(Song_Compiler.singer)