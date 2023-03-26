'''#2

n = input("Введите число: ")
s = 0
for i in str(n):
    s += int(i)
print(s)

#4 4*a = c, 2*a + c = s => a = S/6, c = 2*s/3
s = int(input("Введите число: "))
a = s/6
c = 2*s/3
print("a = " + str(a) + " b = " + str(a) + " c = " + str(c))

#6
n = input("Введите число: ")
s1 = s2 = 0
for i in str(n)[:3]:
    s1 += int(i)
for i in str(n)[3:]:
    s2 += int(i)

if s1 == s2:
    print("Y")
else:
    print("N")
'''
#8
