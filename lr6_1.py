"""
31.Составьте все возможные К разрядные целые числа из четных цифр.
1 часть:
"""
K = int(input("Введите количество разрядов: "))
digits = [0, 2, 4, 6, 8]  # четные цифры

# генерируем все возможные К-разрядные числа из четных цифр
numbers = []
for i in range(len(digits)):
    numbers.append((digits[i],))
for j in range(K-1):
    new_numbers = []
    for number in numbers:
        for digit in digits:
            new_numbers.append(number + (digit,))
    numbers = new_numbers
print(numbers)
print(len(numbers))


