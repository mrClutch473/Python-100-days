for p in range(0,21):
    for k in range(0, 34):
        for c in range(0,101):
            moneyF = 100 - p * 5 - k * 3 - c * 1
            kolvoKurF = 0 + p + k + c*3
            if moneyF == 0 and kolvoKurF == 100:
                print("Petuxov: " + str(p) + " Kur: " + str(k) + " Ciplyat: " + str(c*3))

