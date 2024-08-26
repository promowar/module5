class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print ('Такого этажа не существует')
        else:
            x = 0
            while x != new_floor:
                x = x+1
                print(x)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

p1 = House('ЖК Эльбрус', 10)
p2 = House('ЖК Акация', 20)

# __str__
print(p1)
print(p2)

# __len__
print(len(p1))
print(len(p2))
