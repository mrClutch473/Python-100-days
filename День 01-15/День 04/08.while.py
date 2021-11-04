"""
Производим вычисление суммы всех чисел четных чисел до 1000: 2 + 4 + 6 + .....+ 996 + 998 + 1000
Название файла '08.while.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-04
"""

sum, num = 0, 2  # создаем 2-ве переменные суммы и  шага и сразу задаем их начальное значение равное нулю и 2-м соотв.
while num <= 1000:  # пока переменная num меньше 1000
    sum += num  # считаем сумму всех чисел на каждом шагу
    num += 2  # увеличиваем на 2 переменную num и переходим к следующему шагу
print(sum)  # после завершения цикла выводим результат переменной sum
