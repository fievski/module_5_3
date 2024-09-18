class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __add__(self, value):
        return self

    def __radd__(self, value):
        return self

    def __iadd__(self, value):
        return self

    def __eq__ (self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__ (self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__ (self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__ (self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__ (self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__ (self, other):
        return self.number_of_floors != other.number_of_floors



h1 = House('ЖК Пристройский', 18)
h2 = House('Сарай на даче', 2)
h1.go_to(5)
h2.go_to(10)
print(h1)
print(h2)
print(len(h1))
print(len(h2))


h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 == h2) # __eq__
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#
#     def say_info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age}')
#
#     def birthday(self):
#         self.age += 1
#         print(f'У меня день рождения, мне теперь {self.age} ')
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
#     def __bool__(self, other):
#         return bool(self.age)
#
# sam = Human('Сёма', 25)
# ben = Human('Ваня', 20)
# if sam:
#     sam.say_info()
# print(sam == ben)
# sam.birthday()
# print(sam == ben)
