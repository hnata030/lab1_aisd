"""
2 часть: усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов
и целевую функцию для оптимизации решения.
Найти все возможные числа, оканчивающиеся 0.
Целевая функция: найти числа с максимальной суммой цифр по модулю 8.
"""
K = int(input("Введите K: ")) 
digits = [0, 2, 4, 6, 8] 
 
#Создаем список всех возможных К-разрядных чисел из четных цифр 
numbers = [] 
for i in range(10**(K-1), 10**K): 
    num_str = str(i) 
    if all(int(digit) in digits for digit in num_str): 
        numbers.append(i) 
 
#Находим все числа, оканчивающиеся на 0 
numbers_ending_with_0 = [num for num in numbers if num % 10 == 0] 
 
#Находим числа с максимальной суммой цифр по модулю 8 
max_sum_mod_8 = 0 
max_sum_mod_8_nums = [] 
for num in numbers: 
    num_sum_mod_8 = sum(int(digit) for digit in str(num)) % 8 
    if num_sum_mod_8 > max_sum_mod_8: 
        max_sum_mod_8 = num_sum_mod_8 
        max_sum_mod_8_nums = [num] 
    elif num_sum_mod_8 == max_sum_mod_8: 
        max_sum_mod_8_nums.append(num) 
 
#Выводим результаты 
print("Все возможные {}-разрядные числа из четных цифр:" 
print(numbers) 
print("Числа, оканчивающиеся на 0:") 
print(numbers_ending_with_0) 
print("Числа с максимальной суммой цифр по модулю 8:") 
print(max_sum_mod_8_nums) # выводим список чисел, так как может быть несколько чисел с максимальной суммой цифр по модулю 8 
 
