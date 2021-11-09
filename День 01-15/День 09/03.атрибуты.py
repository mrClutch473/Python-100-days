"""
Python 3.9 Использование атрибутов
-Используйте существующие методы для определения аксессоров / модификаторов / удалителей
Название файла '03.атрибуты.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-09
"""


class Car(object):  # создаем класс

    def __init__(self, brand, max_speed):  # инициализация класса
        self.set_brand(brand)  # обращение к методу-сеттеру (опеределения значения атрибута)
        self.set_max_speed(max_speed)  # обращение к методу-сеттеру (опеределения значения атрибута)

    def get_brand(self):  # метод позволяет обратится к бренду машины напрямую
        return self._brand  # выводит значение марки машины

    def set_brand(self, brand):  # метод позволяет изменить марку машины напрямую
        self._brand = brand  # переопределяет значение атрибута марки машины

    def get_max_speed(self):  # метод позволяет обратится к макс.скорости машины напрямую
        return self._max_speed  # выводит значение макс.скорости машины

    def set_max_speed(self, max_speed):  # метод позволяет изменить макс.скорость машины напрямую
        if max_speed < 0:  # если значение макс. скорости меньше 0
            raise ValueError('Введено не верное значение максимальной скорости автомобиля')
        self._max_speed = max_speed  # переопределяет значение макс.скорости марки машины

    def __str__(self):  # метод выводит строчное значение объекта
        return 'машина: [марка=%s, макс. скорость=%d]' % (self._brand, self._max_speed)  # возвращает строчное значение

    # Используйте существующие модификаторы и аксессоры для определения атрибутов
    brand = property(get_brand, set_brand)  # вышеописанные методы связываются как свойство brand
    max_speed = property(get_max_speed, set_max_speed)  # вышеописанные методы связываются как свойство max_speed


car = Car('QQ', 120)  # создаем объект
print(car)  # выводит информацю о объекте
# ValueError
# car.max_speed = -100
car.max_speed = 320  # переопределяет мак. скорость объекта
car.brand = "Benz"  # перепределяет маку машины
print(car)  # выводит информацю о объекте
print(Car.brand)  # выводит информацю о методе класса - свойство по адресу
print(Car.brand.fget)  # выводит информацю о методе класса - функция по адресу
print(Car.brand.fset)  # выводит информацю о методе класса - функция по адресу
