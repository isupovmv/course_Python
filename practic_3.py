import random
#16

n = int(input("Введите число N: "))
l = []
for i in range(n):
    l.append(random.randint(1, n)) 
print(l)

x = int(input("Введите искомое число X: "))

#способ 1
k = 0
for i in range(len(l)):
    if l[i] == x:
        k += 1

print(k)
#способ 2
l1 = [i for i in l if i == x]
print(len(l1))

#18
n = int(input("Введите число N: "))
l = []
for i in range(n):
    l.append(random.randint(1, n)) 
print(l)

x = int(input("Введите искомое число X: "))

delta = x
for i in l:
    if abs(x - i) < delta:
        delta = abs(x - i)
        k = i
print(k)