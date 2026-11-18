# SG11 Polymorphism Activity 2
## Name: Christine Joyce S. Astillero
## Section: 9 - Magnesium
## Date: 11/18/2026
## School Year: 2026-2027

1. Duck typing is a programming concept in which it focuses on what the objects can do rather than what it actually is. in duck typing, the suitability of the objects are based on its methods and properties and if the methods can be used in its program. Inheritance is not necessary in this concept because it just needs the same methods/properties regardless if it came from a parent class or not. the Car class needs to have the same method as both the Dog and Cat class, it does not need to be inherited from the animal class because it will just need the same method name as the other two classes that will be used in the loop.

2.
``` Python
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone: 
    def move(self):
        print("The drone flies in the sky")

def start_trip(vehicle):
    vehicle.move()

car1 = Car()
boat1 = Boat()
drone1 = Drone()

start_trip(car1)
start_trip(boat1)
start_trip(drone1)

```


3. The code in 2.2 demonstrates polymorphism by having methods 
