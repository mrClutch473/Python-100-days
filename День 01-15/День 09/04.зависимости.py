"""
Python 3.10 Зависимости между объектами и перегрузкой оператора
Название файла '04.зависимости.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-07
"""


class Car(object):  # создаем класс

    def __init__(self, brand, max_speed):  # метод инициализации (на входе 2 аргумента)
        self._brand = brand  # определяем значение атрибута марки машины = принимаему аргументу
        self._max_speed = max_speed  # определяем значение атрибута макс. скорости = принимаему аргументу
        self._current_speed = 0   # определяем значение атрибута скорости = 0

    @property  # геттер
    def brand(self):  # метод позволяет обратится к бренду машины напрямую
        return self._brand  # выводит значение марки машины

    def accelerate(self, delta):  # метод ускорения на входе 1 аргумент
        self._current_speed += delta  # увеличивает атрибут скорости на величину аргумента
        if self._current_speed > self._max_speed:  # если скорость больше максимальной скорости
            self._current_speed = self._max_speed  # скорость = максимальной скорости

    def brake(self):  # метод переопределения текущей скорости
        self._current_speed = 0  # переопределяет атрибут текущей скорости = 0

    def __str__(self):  # метод строчного представления
        return '%s текущую скорость %d' % (self._brand, self._current_speed)


class Student(object):  # определяем класс

    def __init__(self, name, age):  # проводим инициализацию класса
        self._name = name  # определяем значение атрибута = принимаемому аргументу
        self._age = age  # определяем значение атрибута = принимаемому аргументу

    @property  # геттер - свойство передачи значения атрибута
    def name(self):
        return self._name

    # Между учеником и машиной существует зависимость - ученик пользуется машиной
    def drive(self, car):  # метод
        print('%s счастливо водил %s по дороге на запад' % (self._name, car._brand))
        car.accelerate(30)  # определяет новое значение текущей скорости
        print(car)  # отображение информации о машине
        car.accelerate(50)  # определяет новое значение текущей скорости
        print(car)  # отображение информации о машине
        car.accelerate(50)  # определяет новое значение текущей скорости
        print(car)  # отображение информации о машине

    def study(self, course_name):  # метод вывода информации о курсе обучения студента
        print('%s изучает %s.' % (self._name, course_name))

    def watch_av(self):  # метод вывода информации о студенте (ограничении по просмотру фильмов)
        if self._age >= 18:
            print('%s смотрит фильмы без ограничений. ' % self._name)
        else:
            print('%s смотрит фильмы с ограничениями. ' % self._name)

    # Перегрузить оператор больше (>)
    def __gt__(self, other):
        return self._age > other._age

    # Перегружаем оператор меньше (<)
    def __lt__(self, other):
        return self._age < other._age


if __name__ == '__main__':  # если программа запущена как главная
    stu1 = Student('Иван', 38)  # определяем объект
    stu1.study('Программирование на Python')  # добавляем информацию по курсу обучения
    stu1.watch_av()  # вызов метода возврастных ограничений
    stu2 = Student('Костя', 15)  # определяем объект
    stu2.study('Мысль и нравственность')  # добавляем информацию по курсу обучения
    stu2.watch_av()  # вызов метода возврастных ограничений
    car = Car('QQ', 120)  # определяем объект
    stu2.drive(car)  # вызов метода вождения, при этом аргументы берутся из 2-х объектов stu2 и car
    print(stu1 > stu2)  # за счет применения методов __gt__ и __lt__ можем сравнивать 2 объекта (по возрасту)
    print(stu1 < stu2)  # за счет применения методов __gt__ и __lt__ можем сравнивать 2 объекта (по возрасту)
