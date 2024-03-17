import time
import keyboard
import GpsEmulator

class Animal:

    def __init__(self) -> None:
        self.id = len(animals)
        self.currentLocation = Point(0,0)
        self.previousLocation = Point(0,0)
        self.path = Line(self.previousLocation, self.currentLocation)
        animals.append(self)

    def __str__(self) -> str:
        return (f"Animal Id : {self.id} \nCurrent Location : ({self.currentLocation}) \nPrevious Location : ({self.previousLocation})")
    
    def move(self):
        self.previousLocation.lat = self.currentLocation.lat
        self.previousLocation.long = self.currentLocation.long

        coords = GpsEmulator.readGpsInput([self.currentLocation.lat, self.currentLocation.long])

        self.currentLocation.lat = coords[0]
        self.currentLocation.long = coords[1]

        self.updatePath()
    
    def updatePath(self):
        self.path = Line(self.previousLocation, self.currentLocation)
    
class Point:

    def __init__(self, lat, long) -> None:
        self.lat = lat
        self.long = long

    def __str__(self) -> str:
        return (f"Lat : {self.lat}, Long : {self.long}")

class Line:

    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2
    
def intersects(line1 : Line, line2 : Line) -> bool:
    x1 = line1.point1.lat
    y1 = line1.point1.long
    x2 = line1.point2.lat
    y2 = line1.point2.long
    x3 = line2.point1.lat
    y3 = line2.point1.long
    x4 = line2.point2.lat
    y4 = line2.point2.long

    t1 = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4))
    t2 = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    t = t1 / t2
    u1 = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2))
    u2 = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    u = u1 / u2
    if 0 <= t and t <= 1 and 0 <= u and u <= 1:
        return True
    return False

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
        animal2.move()
        print(animal2)
        print(intersects(animal1.path, animal2.path))
        time.sleep(1)

except KeyboardInterrupt:
    exit()