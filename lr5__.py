"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени
вычисления представить в табличной и графической форме.
F(1) = 2; G(1) = 1; F(n) = F(n–1) – G(n–1), G(n) = F(n–1) + G(n–1), при n >=2
"""
from timeit import timeit
import matplotlib.pyplot as plt

a = []
b = []
c = []
def rec_f(n):
    if n == 1:
        return 2
    return rec_f(n-1) - rec_g(n-1)
        
def rec_g(n):
    if n == 1:
        return 1
    return rec_f(n-1) + rec_g(n-1)
def iter_f(n):
    f = 2
    g = 1
    for i in range(2,n+1):
        new_f = f - g
        new_g = f + g
        f = new_f
        g = new_g
    return f
def iter_g(n):
    f = 2
    g = 1
    for i in range(2,n+1):
        new_f = f - g
        new_g = f + g
        f = new_f
        g = new_g
    return g

n = int(input("Введите n: "))

print("n | Рекурсивное время | Итерационное время ")
print('-' * 62)

for i in range(1, n+1):
    tm1 = 'from __main__ import rec_f'
    rctm = 'rec_f('+ str(i)+')'
    tm2 = 'from __main__ import iter_f'
    itrtm = 'iter_f('+ str(i)+')'
    a.append(timeit(setup=tm1, stmt=rctm, number=20000))
    b.append(timeit(setup=tm2, stmt=itrtm, number=20000))
    c.append(i)
    print(str(i) + '|' + str(round(timeit(setup=tm1, stmt=rctm, number=20000),17)) + '|'+ str(round(timeit(setup=tm2, stmt=itrtm, number=20000),17)))

y1 = a
y2 = b
x = c
plt.xlabel('Число n')
plt.ylabel('Время вычисления')
plt.plot(x, y1, label='Рекурсивно')
plt.plot(x, y2, label='Итеративно')
plt.legend()
plt.show()
