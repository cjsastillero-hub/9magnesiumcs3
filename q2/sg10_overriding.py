# SG10 - Method Overriding
## Name: Christine Joyce S. Astillero
## Section: 9-Magnesium
## Date: 11/4/2026
## School Year: 2026-2027

class Animal:
  def __init__(self, name):
    self.__name = name
    
  @property
  def name(self):
    return self.__name

  def eat(self):
    print(self.name, "is eating.")
  def make_sound(self):
    print(self.name, "makes a sound")

class Lion(Animal):
  def make_sound(self):
    print(self.name, "roars loudly!")
    
  def eat(self):
    print(self.name, "eats fresh meat.")

class Elephant(Animal):
  def make_sound(self):
    print(self.name, "trumpets!")

  def eat(self):
    print(self.name, "eats grass and fruits.")

class Monkey(Animal):
  def make_sound(self):
    print(self.name, "chatters!")

  def eat(self):
    print(self.name, "eats bananas.")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

animals = [lion, elephant, monkey]

for ani in animals:
  ani.make_sound()
  ani.eat()
  print("-----")

          
  
  
