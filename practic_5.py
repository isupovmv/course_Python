#26
def my_func(a, b):
    if b > 1:
        a = a * my_func(a, b - 1)
    return a

print(my_func(2, 5))

#28 
def my_func(a, b):
    if b > 0:
        a = 1 + my_func(a, b - 1)
    return a

print(my_func(2, 5))
