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
       
Song1 = Pop_Songs("Kid and Leveret", 2024, 180, "Yaelokre")

Song2 = Pop_Songs("From Now On", 2023, 182, "Hugh Jackman")

print ("--BEFORE--")
print("")

print(f"{Song1.title}, {Song1.singer}")
print(f"{Song2.title}, {Song2.singer}")

Song1.ChangeSinger("Yeng Constantino")

print("")

print("--AFTER--")
print("")
print(f"{Song1.title}, {Song1.singer}")
print(f"{Song2.title}, {Song2.singer}")