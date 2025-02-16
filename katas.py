# Родительский класс
class Animal:
    def __init__(self, name):
        self.name = name  # Атрибут (свойство)

    def speak(self):
        print(f"{self.name} издает звук!")

# Дочерний класс
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора родительского класса
        self.breed = breed  # Атрибут для породы собаки

    def speak(self):  # Переопределение метода родительского класса
        print(f"{self.name} говорит: Гав!")

# Создаем объект дочернего класса
dog = Dog("Бобик", "Терьер")
dog.speak()  # Бобик говорит: Гав!
class Cat(Animal):
    pass  # Мы не переопределяем метод, он будет таким, как в родительском классе

cat = Cat("Мурка")
cat.speak()  # Мурка издает звук!
