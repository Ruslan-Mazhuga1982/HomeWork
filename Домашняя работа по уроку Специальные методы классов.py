class house():
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.floors = floors

    floors = 8
    for i in range(floors):
        i = floors
        numberOfFloors += floors
        print(numberOfFloors)
