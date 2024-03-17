import time
import keyboard
import GpsEmulator

class Animal:

    def __init__(self, field) -> None:
        self.id = len(animals)
        self.currentLocation = Point(0,0)
        self.previousLocation = Point(0,0)
        self.path = Line(self.previousLocation, self.currentLocation)
        animals.append(self)
        self.field = field
        self.contained = True

    def __str__(self) -> str:
        return (f"Animal Id : {self.id} \nCurrent Location : ({self.currentLocation}) \nPrevious Location : ({self.previousLocation})\nContained : {self.contained}")
    
    def move(self):
        self.previousLocation.lat = self.currentLocation.lat
        self.previousLocation.long = self.currentLocation.long

        coords = GpsEmulator.readGpsInput([self.currentLocation.lat, self.currentLocation.long])

        self.currentLocation.lat = coords[0]
        self.currentLocation.long = coords[1]

        self.updatePath()

        self.field.contains(self)
    
    def updatePath(self):
        self.path = Line(self.previousLocation, self.currentLocation)

class Field:

    def __init__(self, points) -> None:
        self.points = points
        self.lines = self.generateLines()
    
    def generateLines(self):
        prevPoint = self.points[0]
        lines = []

        for i in range(len(self.points) - 1):
            currentPoint = self.points[i+1]

            lines.append(Line(prevPoint, currentPoint))

            prevPoint = currentPoint
        
        lines.append(Line(self.points[-1], self.points[0]))
        
        return lines

    def contains(self, animal):
        for line in self.lines:
            if(intersects(line, animal.path)):
                animal.contained = not animal.contained
                print(f"Animal Containment : {animal.contained}")
                return animal.contained

        return animal.contained

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
    
    def __str__(self) -> str:
        return (f"Point 1 : {self.point1}, Point 2 : {self.point2}")
    
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
    try:
        t = t1 / t2
    except ZeroDivisionError:
        return False
    u1 = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2))
    u2 = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    u = u1 / u2
    if 0 <= t and t <= 1 and 0 <= u and u <= 1:
        return True
    return False

animals = []


point1 = Point(-1,1)
point2 = Point(1,1)
point3 = Point(1,-1)
point4 = Point(-1,-1)

field = Field([point1,point2,point3,point4])

for line in field.lines:
    print(line)

animal1 = Animal(field)
animal2 = Animal(field)

print(animal1.field.lines)

try:
    while True:
        animal1.move()
        print(animal1)
        time.sleep(1)

except KeyboardInterrupt:
    exit()