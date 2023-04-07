# Шеснадцатиричные нечетные числа, не превышающие 4096 и содержащие количество цифр равное сумме первой
# и последней цифр. Вывести числа и их количество. Минимальное число вывести прописью.

import re
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

d = []
with open('posl.txt', 'r') as f:
    line = f.readline().split()
    if line:
        for i in line:
            b = []
            a = re.findall(r'\b([1-9a-fA-F]{1,3})(?<!00)\b', i)
            for i in a: b.append(str(int(i, 16)))
            for i in b:
                c = re.findall(r'\b[0-9]*[13579]\b', i)
                if c:
                    if len(c[0]) == int(c[0][0]) + int(c[0][-1]):
                        d.append(int(c[0]))
    else:
        print('\nФайл в директории проекта пустой')
        exit()
if len(d) > 0:
    print('Числа:', *d)
    print('Количество чисел:', len(d))
    print('Минимальное число: ', end='')
    h = str(min(d))
    e = len(h)
    for i in range(len(h)):
        if int(h[i]) != 0:
            if e == 4:
                print(tho[int(h[i])], end=' ')
                e -= 1
            elif e == 3:
                print(hun[int(h[i])], end=' ')
                e -= 1
            elif e == 2:
                if int(h[-1]) != 0 and int(h[i]) == 1:
                    print(doz1[int(h[i:])], end=' ')
                    e -= 2
                else:
                    print(doz[int(h[i])], end=' ')
                    e -= 1
            elif e == 1:
                print(num[int(h[i])], end=' ')
                e -= 1
        else:
            e -= 1
else:
    print('Чисел подходящих под условия не найдено')

