"""
Написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода.
Писать с помощью кода из лаб.работы №6(2 часть).
Лаб.работа №6: Составить все возможные К разрядные целые числа из четных цифр.
Найти все возможные числа, оканчивающиеся 0.
Целевая функция: найти числа с максимальной суммой по модулю 8.
"""

class NumberFinder:
    def __init__(self):
        self.K = 0
        self.digits = [0, 2, 4, 6, 8]
        self.numbers = []
        self.numbers_ending_with_0 = []
        self.max_sum_mod_8 = 0
        self.max_sum_mod_8_nums = []
    #Ввод К
    def get_input(self):
        while True:
            try:
                self.K = int(input("Введите K: "))
                if self.K < 1 or self.K > 6:
                    raise ValueError
                break
            except ValueError:
                print("Введите положительное целое число не больше 6.")
    #Создание К разрядных чисел
    def generate_numbers(self):
        for i in range(10**(self.K-1), 10**self.K):
            num_str = str(i)
            if all(int(digit) in self.digits for digit in num_str):
                self.numbers.append(i)
    # Числа, оканчивающиеся на 0
    def find_numbers_ending_with_0(self):
        self.numbers_ending_with_0 = [num for num in self.numbers if num % 10 == 0]
    # Нахождение чисел с максимальной суммой цифр по модулю 8
    def find_max_sum_mod_8(self):
        for num in self.numbers:
            num_sum_mod_8 = sum(int(digit) for digit in str(num)) % 8
            if num_sum_mod_8 > self.max_sum_mod_8:
                self.max_sum_mod_8 = num_sum_mod_8
                self.max_sum_mod_8_nums = [num]
            elif num_sum_mod_8 == self.max_sum_mod_8:
                self.max_sum_mod_8_nums.append(num)
    #Результат
    def print_results(self):
        print("Все числа:", self.numbers)
        print("Числа, оканчивающиеся на 0:", self.numbers_ending_with_0)
        print("Числа с максимальной суммой цифр по модулю 8:", self.max_sum_mod_8_nums)

number_finder = NumberFinder()
number_finder.get_input()
number_finder.generate_numbers()
number_finder.find_numbers_ending_with_0()
number_finder.find_max_sum_mod_8()
number_finder.print_results()

