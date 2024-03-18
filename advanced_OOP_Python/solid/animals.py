from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        ...

    def get_species(self):
        return self.__class__.__name__.lower()


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Chicken(Animal):
    def make_sound(self):
        return 'cluck'


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
