"""
2 часть: усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов
и целевую функцию для оптимизации решения.
Найти все возможные числа, оканчивающиеся 0, и сумма которых по модулю  равна 8.
Целевая функция: минимизация количества пар чисел, удовлетворяющих условиям.
"""

K = int(input("Введите количество разрядов: "))  
digits = [0, 2, 4, 6, 8]  
numbers = []  

# генерируем все возможные К-разрядные числа из четных цифр
for i in range(len(digits)):
    numbers.append(digits[i])
for j in range(K-1):
    new_numbers = []
    for number in numbers:
        for digit in digits:
            new_numbers.append(number * 10 + digit)
    numbers = new_numbers

# находим все возможные числа, оканчивающиеся на 0 и сумма цифр которых по модулю равна 8
target_numbers = []
for number in numbers:
    if number % 10 == 0 and sum(int(digit) for digit in str(number)) % 10 == 8:
        target_numbers.append(number)

# выводим результаты
print("Все возможные числа из четных цифр:", numbers)
print("Все возможные числа, оканчивающиеся на 0, и сумма цифр которых по модулю равна 8:", target_numbers)
