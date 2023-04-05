#34
def my_func(p_str):
    gl = 'аеёиоуыэюя'
    l = []
    res = []
    l = p_str.split(" ")
    
    for phrase in l:
        kol = 0
        for symb in phrase:
            if symb in gl:
                kol += 1
        res.append(kol)

    return len(res) == res.count(res[0])    #длина списка равна количеству элементов равных первому

s = 'пара-ра-рам рам-пам-папам па-ра-па-даа'

if my_func(s):
    print('Парам пам-пам')
else:
    print('Пам парам')

#36
def print_operation_table(operation, num_rows=6, num_columns=6):
    m = []
    for i in range(1, num_rows + 1):
        m_str = []
        for j in range(1, num_columns + 1):
           m_str.append(operation(i, j))
        m.append(m_str)
    print(m) 


print_operation_table(lambda x, y: x * y, 4, 4)