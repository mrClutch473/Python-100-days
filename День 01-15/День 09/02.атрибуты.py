"""
Python 3.10 Использование атрибутов
-Аксессор / модификатор / удалитель
-Используйте __slots__ для ограничения атрибутов
Название файла '02.атрибуты.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-07
"""


class Car(object):  # создаем класс
    # Объекты класса Car могут быть привязаны только к атрибутам '_brand' и '_max_speed'
    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):  # метод инициализации (на входе 2 аргумента)
        self._brand = brand  # определяем значение атрибута марки машины = принимаему аргументу
        self._max_speed = max_speed  # определяем значение атрибута макс. скорости = принимаему аргументу

    @property  # геттер
    def brand(self):  # метод позволяет обратится к бренду машины напрямую
        return self._brand  # выводит значение марки машины

    @brand.setter  # сеттер
    def brand(self, brand):  # метод позволяет изменить марку машины напрямую
        self._brand = brand  # переопределяет значение атрибута марки машины

    @brand.deleter  # очищает значение атрибута бренда машины
    def brand(self):
        del self._brand

    @property  # геттер
    def max_speed(self):  # метод позволяет обратится к макс.скорости машины напрямую
        return self._max_speed  # выводит значение макс.скорости машины

    @max_speed.setter  # сеттер
    def max_speed(self, max_speed):  # метод позволяет изменить макс.скорость машины напрямую
        if max_speed < 0:  # если значение макс. скорости меньше 0
            raise ValueError('Введено не верное значение максимальной скорости автомобиля')
        self._max_speed = max_speed  # переопределяет значение макс.скорости марки машины

    def __str__(self):  # метод выводит строчное значение объекта
        return 'машина: [марка=%s, макс. скорость=%d]' % (self._brand, self._max_speed)  # возвращает строчное значение


car = Car('QQ', 120)  # создаем объект
print(car)  # выводит информацю о объекте
# ValueError
# car.max_speed = -100
car.max_speed = 320  # переопределяет мак. скорость объекта
car.brand = "Benz"  # перепределяет маку машины
# Следующий код вызовет исключение после использования ограничения атрибута __slots__
# car.current_speed = 80
print(car)  # выводит информацю о объекте
# Если предоставляется средство удаления, следующий код может быть выполнен
# del car.brand
# Реализация атрибутов
print(Car.brand)  # выводит информацю о методе класса - свойство по адресу
print(Car.brand.fget)  # выводит информацю о методе класса - функция по адресу
print(Car.brand.fset)  # выводит информацю о методе класса - функция по адресу
print(Car.brand.fdel)  # выводит информацю о методе класса - функция по адресу

