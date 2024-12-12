import random

pr = True

while pr:
    print("1. Бросить кости 2.Выход")
    chs = int(input())
    if chs == 1:
        k1 = random.randint(1,6)
        k2 = random.randint(1, 6)
        print("1 кубик: " +str(k1) + " 2 кубик: " + str(k2))
        if k1+k2 == 7 or k1+k2 == 11:
            print("Выйграл Игрок")
        elif k1 + k2 == 2 or k1 + k2 == 3 or k1+k2 == 12:
            print("Выйграл Крупье")
        else:
            print("Ничья, продолжайте бросать")
    else:
        pr = False