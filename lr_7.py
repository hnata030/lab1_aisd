"""
Написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода
Писать с помощью кода из лаб.работы №6(2 часть)
"""

class NumberFinder:
    def __init__(self):
        self.K = 0
        self.digits = [0, 2, 4, 6, 8]
        self.numbers = []
        self.numbers_ending_with_0 = []
        self.max_sum_mod_8 = 0
        self.max_sum_mod_8_nums = []

    def get_input(self):
        self.K = int(input("Введите K: "))

    def generate_numbers(self):
        for i in range(10**(self.K-1), 10**self.K):
            num_str = str(i)
            if all(int(digit) in self.digits for digit in num_str):
                self.numbers.append(i)

    def find_numbers_ending_with_0(self):
        self.numbers_ending_with_0 = [num for num in self.numbers if num % 10 == 0]

    def find_max_sum_mod_8(self):
        for num in self.numbers:
            num_sum_mod_8 = sum(int(digit) for digit in str(num)) % 8
            if num_sum_mod_8 > self.max_sum_mod_8:
                self.max_sum_mod_8 = num_sum_mod_8
                self.max_sum_mod_8_nums = [num]
            elif num_sum_mod_8 == self.max_sum_mod_8:
                self.max_sum_mod_8_nums.append(num)

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

