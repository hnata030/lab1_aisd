"""
Шеснадцатиричные нечетные числа, не превышающие 409610 и содержащие количество цифр равное сумме первой и последней цифр. 
Вывести числа и их количество. 
Минимальное число вывести прописью.
"""
num = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
       6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
doz = {0: '', 1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок',
       5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
       8: 'восемьдесят', 9: 'девяносто'}
doz1 = {0: '', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
        14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
        17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
hun = {0: '', 1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
       5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот',
       9: 'девятьсот'}
tho = {1: 'одна тысяча', 2: 'две тысячи', 3: 'три тысячи', 4: 'четыре тысячи'}
max_buffer_len = 100
buffer_len = 1
work_buffer = ''
work_buffer_len = buffer_len
c = []
with open('1_.txt', mode='r') as f:
    a = f.read(buffer_len)
    if not a:
        print('\n Файл в директории проекта пустой')
        exit()
    while a:
        while '0' <= a <= '9' or a.isalpha():
            if '0' <= a <= '9' or a.isalpha():
                work_buffer += a
            a = f.read(buffer_len)
        if len(work_buffer) > 0:
            try:
                b = int(work_buffer, 16)
                if b <= 4096 and b % 2 != 0 and len(str(b)) == int(str(b)[0]) + int(str(b)[-1]):
                    c.append(b)
            except Exception:
                continue
        work_buffer = ''
        a = f.read(buffer_len)
print('Числа:', *c)
print('Количество чисел:', len(c))
print('Минимальное число: ', end='')
d = ''
if len(c) > 0:
    d = str(min(c))
    e = len(d)
for i in range(len(d)):
    if int(d[i]) != 0:
        if e == 4:
            print(tho[int(d[i])], end=' ')
            e -= 1
        elif e == 3:
            print(hun[int(d[i])], end=' ')
            e -= 1
        elif e == 2:
            if int(d[-1]) != 0 and int(d[i]) == 1:
                print(doz1[int(d[i:])], end=' ')
                e -= 2
            else:
                print(doz[int(d[i])], end=' ')
                e -= 1
        elif e == 1:
            print(num[int(d[i])], end=' ')
            e -= 1
    else:
        e -= 1
