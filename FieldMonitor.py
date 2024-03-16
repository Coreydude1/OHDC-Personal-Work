import time
import keyboard
import GpsEmulator

class Animal:

    def __init__(self) -> None:
        self.id = len(animals)
        self.currentLocation = [0,0]
        self.previousLocation = [0,0]
        animals.append(self)

    def __str__(self) -> str:
        return (f"Id : {self.id} \nCurrent Location : {self.currentLocation} \nPrevious Location : {self.previousLocation}")

animals = []

animal1 = Animal()
animal2 = Animal()

for animal in animals:
    print(animal)

try:
    while True:
        animal1.previousLocation = animal1.currentLocation
        animal1.currentLocation = GpsEmulator.readGpsInput(animal1.currentLocation)
        print(animal1)
        time.sleep(0.5)

except KeyboardInterrupt:
    exit()