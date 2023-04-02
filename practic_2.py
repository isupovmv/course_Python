#10

import random
n = int(input("Введите число монет: "))
side1 = side2 = v = 0
for i in range(n):
    v = random.randint(0, 1) 
    print(v)

    if v == 0:
        side1 += 1
    else:
        side2 += 1

v = side1 
if side1 > side2:
    v = side2

print(f'нужно перевернуть {v} монет')

#12 x+y=s, x*y=p
s = int(input("Сумма чисел: "))
p = int(input("Произведение: "))

b = True
for x in range(1001):
    if b:
        for y in range(1001):
            if b:
                if x * y == p and x + y == s:
                    print(f'Задумали числа {x}, {y}')
                    b = False

if b:
    print("Числа не найдены")

#14
n = int(input("Введите число N: "))

x = 2
i = 2
while (x < n):
    print(x)
    x = 2 * i
    i += 1





