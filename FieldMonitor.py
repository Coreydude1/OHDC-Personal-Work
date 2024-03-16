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
        return (f"Animal Id : {self.id} \nCurrent Location : ({self.currentLocation}) \nPrevious Location : ({self.previousLocation})")
    
    def move(self):
        self.previousLocation.lat = self.currentLocation.lat
        self.previousLocation.long = self.currentLocation.long

        coords = GpsEmulator.readGpsInput([self.currentLocation.lat, self.currentLocation.long])

        self.currentLocation.lat = coords[0]
        self.currentLocation.long = coords[1]
    
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