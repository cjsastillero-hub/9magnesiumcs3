class Singer:
    def __init__(self, SingerSong):
        self.SingerSong = SingerSong

    def ChangeSinger(self, NewSinger ):
        self.SingerSong = NewSinger



class Pop_Songs(Singer):
    def __init__(self, SingerSong, TitleSong, PersonalRating, SingerCollaborator):
        super().__init__(SingerSong)

        self.PersonalRating = PersonalRating
        self.TitleSong = TitleSong
        self.Collaborator = SingerCollaborator

    def ReturnTitle(self):
           print(f"The title of the song is {self.TitleSong}")
    def loopsong(self, NumberOfLoops):
           print(f"The song will be looped for this many times: {NumberOfLoops}")


print("----INHERITANCE----")
print("")
Singer1 = Singer( "Jason Derulo")
PopSong1 = Pop_Songs("Jason Derulo", "Savage", 6.5, Singer1)

print("Parent attribute:")
print(f"Singer: {Singer1.SingerSong}")

print("---------------------")

print("Child Object:")
print("Pop Song 1")
print(f"Singer: {PopSong1.SingerSong}")

print("")
print("----AGGREGATION----")
print("")
Singer2 = Singer("Zendaya")
PopSong2 = Pop_Songs("Zack Effron", "Rewrite The Stars", 9.0, Singer2)

print("An already existing object (Singer 2) is being contained in PopSong2 from the class Pop_Songs. Singer 2 is being contained in the variable 'Collaborator'.")
print(f"Title: {PopSong2.TitleSong}")
print(f"Singer: {PopSong2.SingerSong}")
print(f"The collaborator of the song/the contained already existing object: {PopSong2.Collaborator.SingerSong}")