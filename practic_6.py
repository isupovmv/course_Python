import random
#30

a1 = int(input("Введите число a1: "))
d = int(input("Введите число d: "))
n = int(input("Введите число N: "))
for i in range(n):
    print(a1 + i * d)

#32
n = int(input("Введите число N: "))
l = []
for i in range(n):
    l.append(random.randint(-n, n)) 
print(l)

min_number = 1
max_number = 25
for i in range(len(l)):
    if min_number <= l[i] <= max_number:
        print(i)