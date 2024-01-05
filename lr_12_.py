'''
Вычислить сумму знакопеременного ряда (|х*2n!|)/(2n)!, где х-матрица ранга к (к и матрица задаются случайным образом),
n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
У алгоритма д.б. линейная сложность.
Операция умножения –поэлементная. Знак первого слагаемого  +.
Вариант 30
'''

import random
import numpy as np
import decimal as de
import math

# Создание матрицы
k = random.randint(1, 10) 
x = np.random.uniform(-1, 1, (k, k))  

t = input("Введите число t от 1 до 100: ") 

# Проверка t на правильность ввода
while True:
    if t.isdigit() and 1 <= int(t) <= 100:  
        t = int(t)  
        break  
    elif not t.isdigit(): 
        t = input("t не является числом, введите его ещё раз: ")
    elif int(t) < 1 or int(t) > 100:  
        t = input("Число t меньше единицы или больше ста, введите его ещё раз: ")

n = 1  
n_factorial = 1 
sign = 1  
result = de.Decimal(0)  
matrix = x 
de.getcontext().prec = t + 60 
fun = de.Decimal(0)  

while abs(result.as_tuple().exponent) < t:  
    fun = de.Decimal(1 * np.linalg.det(np.multiply(matrix, 2 * n_factorial))) * de.Decimal((1 / math.factorial(2*n))) 
    result = result + (sign * fun) 

    n += 1  
    n_factorial *= n  
    sign = -sign  
# Вывод
print(x)  
print(f"Результат: {result:.{t}f}")  
