# 1-mashq
class Test:
    x = 10

print(Test.x)
# 2-mashq
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2,3))
# 3-mashq
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
# 4-mashq
class Account:
    def __init__(self):
        self.__money = 100

    def get_money(self):
        return self.__money
# 5-mashq
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
