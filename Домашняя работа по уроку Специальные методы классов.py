# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors
# Полученный код напишите в ответ к домашему заданию
class House():
    # numberOfFloors = 0
    # floors = 8

    def __init__(self):
        self.numberOfFloors = 0


    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        #print(self.numberOfFloors)


h1 = House()
#print(h1.numberOfFloors)
h1.setNewNumberOfFloors(15)
print(h1.numberOfFloors)
