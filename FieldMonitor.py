import time
import keyboard
import GpsEmulator

class Animal:

    def __init__(self) -> None:
        self.id = len(animals)
        self.currentLocation = Point(0,0)
        self.previousLocation = Point(0,0)
        animals.append(self)

    def __str__(self) -> str:
        return (f"Id : {self.id} \nCurrent Location : ({self.currentLocation}) \nPrevious Location : ({self.previousLocation})")
    
    def move(self):
        animal1.previousLocation.lat = animal1.currentLocation.lat
        animal1.previousLocation.long = animal1.currentLocation.long

        coords = GpsEmulator.readGpsInput([self.currentLocation.lat, self.currentLocation.long])

        animal1.currentLocation.lat = coords[0]
        animal1.currentLocation.long = coords[1]
    
class Point:

    def __init__(self, lat, long) -> None:
        self.lat = lat
        self.long = long

    def __str__(self) -> str:
        return (f"Lat : {self.lat}, Long : {self.long}")

class Line:

    def __init__(self, points) -> None:
        self.points = points
    

animals = []

animal1 = Animal()
animal2 = Animal()

for animal in animals:
    print(animal)

try:
    while True:
        animal1.move()
        print(animal1)
        time.sleep(1)

except KeyboardInterrupt:
    exit()