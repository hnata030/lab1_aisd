"""
Шеснадцатиричные нечетные числа, не превышающие 4096 и содержащие количество цифр равное сумме первой и последней цифр.
Вывести числа и их количество. Минимальное число вывести прописью.
"""
delimiter = " "
digits_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15} 
nums_10 = list() 
words = {0: 'ноль', 
         1: 'один', 
         2: 'два', 
         3: 'три', 
         4: 'четыре', 
         5: 'пять', 
         6: 'шесть', 
         7: 'семь', 
         8: 'восемь', 
         9: 'девять', 
         10: 'десять', 
         11: 'одиннадцать', 
         12: 'двенадцать', 
         13: 'тринадцать', 
         14: 'четырнадцать', 
         15: 'пятьнадцать', 
         16: 'шестьнадцать', 
         17: 'семьнадцать', 
         18: 'восемьнадцать', 
         19: 'девятьнадцать', 
         20: 'двадцать', 
         30: 'тридцать', 
         40: 'сорок', 
         50: 'пятьдесят', 
         60: 'шестьдесят', 
         70: 'семьдесят', 
         80: 'восемьдесят', 
         90: 'девяносто', 
         100: 'сто', 
         200: 'двести', 
         300: 'триста', 
         400: 'четыреста', 
         500: 'пятьсот', 
         600: 'шестьсот', 
         700: 'семьсот', 
         800: 'восемьсот', 
         900: 'девятьсот', 
         1000: 'одна тысяча', 
         2000: 'две тысячи', 
         3000: 'три тысячи', 
         4000: 'четыре тысячи' 
         } 
 
 
def convert_to_decimal(number16): 
    result = 0 
    i = 0 

    number16 = number16.upper() 
    for digit in number16[::-1]:  # reverse 
        if digit in digits_dict.keys(): 
            result += digits_dict[digit] * (16 ** i) 
        else: 
            try: 
                result += int(digit) * (16 ** i) 
            except ValueError: 
                return -1 
        i += 1 

    return result 
 

def num2words(num): 
    z = num // 100 
    s = words[z * 100] 
 
    y = num % 100 
    if num<20: 
        s = words[y] 
    elif y <= 20: 
        s = s + ' ' + words[y] 
    else: 
        m = y // 10 
        n = y % 10 
        s = s + ' ' + words[m * 10] + ' ' + words[n] 
    return s 
 

with open('input.txt', 'r') as f:
    while True: 
        block = f.read(1024) 
        if not block: 
            break 
        nums = block.split(delimiter) 
        for num in nums: 
            num = convert_to_decimal(num) 
            if num == -1: 
                continue 
            if num < 4096 and len(str(num)) == (int(str(num)[0]) + num % 10) and num % 2 == 1: 
                nums_10.append(num) 

    for num in nums_10: 
        print("Числа:"num)  ## числа 
    print() 
    print("Количество чисел:", len(nums_10))  ## количество чисел 
 
    if len(nums_10) != 0: 
        print("Минимальное число:", num2words(min(nums_10)))  ##вывод минимума прописью
