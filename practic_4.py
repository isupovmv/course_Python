import random
#22

n = int(input("Введите число N: "))
m = int(input("Введите число M: "))
l1 = [] 
l2 = []
for i in range(n):
    l1.append(random.randint(1, n))
for i in range(m):
    l2.append(random.randint(1, m))
print(l1)
print(l2)
print("Сортировка:")
l1 = l1 + l2
l1 = list(set(l1))
l1 = sorted(l1, reverse=True)
print(l1)

#24
n = int(input("Введите число кустов N: "))
l = []
for i in range(n):
    l.append(random.randint(1, n))
print(l)

k = l[0]
for i in range(n - 1):
    if l[i - 1] + l[i] + l[i + 1] > k:
        k = l[i - 1] + l[i] + l[i + 1]
print(k)
