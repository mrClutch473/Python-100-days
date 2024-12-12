n1 = int(input())
n2 = int(input())

for i in range(n1,n2+1):
    l = i % 10
    m = i // 10 % 10
    h = i // 100
    if (h**3 + m**3 + l**3) == i:
        print(i)
    #print(str(h)+" "+str(m)+" "+str(l))