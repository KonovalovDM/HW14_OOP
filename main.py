# Создаем базовый класс
class Pet:
    def __init__(self, name, species, age, gender):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__gender = gender

    def get_info(self):
        print(f'Имя: {self.__name}, Вид: {self.__species}, Возраст: {self.__age}, Пол: {self.__gender}')

    def make_sound(self):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

# Наследование: создаем подклассы домашних питомцев
class Dog(Pet):
    def __init__(self, name, species, age, gender, breed):
        super().__init__(name, species, age, gender)
        self.__breed = breed

    def make_sound(self):
        print(f'{self.species} по кличке {self.name} лает "Гав!"')

class Cat(Pet):
    def __init__(self, name, species, age, gender, color):
        super().__init__(name, species, age, gender)
        self.__color = color

    def make_sound(self):
        print(f'{self.species} по кличке {self.name} мяучит "Мяу!"')

# Функция для демонстрации полиморфизма
def pet_sounds(pets):
    for pet in pets:
        pet.make_sound()

# Композиция, создаем Зоомагазин
class Zoo:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f"{pet.species} по кличке {pet.name} добавлена в группу животных Зоомагазина")

# Создаем экземпляры классов домашних питомцев
zoo = Zoo()
dog = Dog("Барон", "Собака", 8, "кобель", "Мастиф")
cat = Cat("Маша", "Кошка", 6, "кошка", "Русская голубая")

# Добавление питомцев в зоомагазин
zoo.add_pet(dog)
zoo.add_pet(cat)

# Демонстрируем полиморфизм
pet_sounds(zoo.pets)

# Выводим информацию о питомцах
dog.get_info()
cat.get_info()