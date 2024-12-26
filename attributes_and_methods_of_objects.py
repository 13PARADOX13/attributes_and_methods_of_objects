class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        self.number_of_floors
        floor = 1
        while floor <= new_floor <= self.number_of_floors:
            print(floor)
            floor += 1
        if new_floor < 1 or new_floor > self.number_of_floors :
            print('Такого этажа не существует')

h1 = House('ЖК Бавария', 13)
h2 = House('Таунхаус', 2)

h1.go_to(7)
h2.go_to(3)