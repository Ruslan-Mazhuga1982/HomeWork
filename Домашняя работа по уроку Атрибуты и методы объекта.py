class House():
    """ Информация о здании """

    def __init__(self, name, number_of_floors, house_number_1, apartments_1):

        self.name = name
        """ Информация о здании """
        self.house_number_1 = house_number_1
        self.number_of_floors_1 = number_of_floors
        self.apartments_1 = apartments_1



    name = 'ЖК Эльбрус'
    house_number_1 = 10
    number_of_floors_1 = 30
    apartments_1 = 96


    def go_to(self, new_floor_1, zapros):
        super().__init__(self)
        self.new_floor_1 = new_floor_1
        self.zapros = zapros

    new_floor_1 = [0, 1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10, 11,
                   12, 13, 14, 15, 16, 17,
                   18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


    """ Запрашиваем информацию о здании и выводим ее на консоль """
    while True:
        zapros = input("Введите номер дома: ")
        if zapros == '10':
            print(name, 'в доме с №', house_number_1, number_of_floors_1, "Этажей", apartments_1, 'Квартир')
        else:
            print('Дома с таким номером в ', name, 'Не существует')
            continue
        while True:
            zapros = int(input("Введите номер Этажа: "))

            if zapros in new_floor_1:
                print("Вы поднялись на нужный этаж")
                break
            else:
                if zapros not in new_floor_1:
                    print('В этом здании Нет такого этажа')
                    break









