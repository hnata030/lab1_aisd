"""
1 часть:
Составить все возможные К разрядные целые числа из четных цифр.
2 часть:
Найти все возможные числа, оканчивающиеся 0.
Целевая функция: найти числа с максимальной суммой по модулю 8.
"""


import tkinter as tk
from tkinter import scrolledtext

def run_program():
    try:
        K = int(input_entry.get())
        if K <= 0:
            raise ValueError("Значение K должно быть положительным.")
        if K > 6:
            raise ValueError("Значение K не может быть больше 6.")

        digits = [0, 2, 4, 6, 8]
        # Создание К-разрядных чисел из четных цифр
        numbers = []
        for i in range(10**(K-1), 10**K):
            num_str = str(i)
            if all(int(digit) in digits for digit in num_str):
                numbers.append(i)
        # Числа, оканчивающиеся на 0
        numbers_ending_with_0 = [num for num in numbers if num % 10 == 0]
        # Нахождение чисел с максимальной суммой цифр по модулю 8
        max_sum_mod_8 = 0
        max_sum_mod_8_nums = []
        for num in numbers:
            num_sum_mod_8 = sum(int(digit) for digit in str(num)) % 8
            if num_sum_mod_8 > max_sum_mod_8:
                max_sum_mod_8 = num_sum_mod_8
                max_sum_mod_8_nums = [num]
            elif num_sum_mod_8 == max_sum_mod_8:
                max_sum_mod_8_nums.append(num)

        # Вывод результата
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"\nЧисла с максимальной суммой цифр по модулю 8:\n")
        for number in max_sum_mod_8_nums:
            result_text.insert(tk.END, f"{number}\n")
        result_text.insert(tk.END, f"Все возможные {K}-разрядные числа из четных цифр:\n")
        for number in numbers:
            result_text.insert(tk.END, f"{number}\n")
        result_text.insert(tk.END, f"\nЧисла, оканчивающиеся на 0:\n")
        for number in numbers_ending_with_0:
            result_text.insert(tk.END, f"{number}\n")
        

    except ValueError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(e))

# Создание главного окна
root = tk.Tk()
root.title("Lr_8")
root.geometry("600x500")

# Создание окна ввода
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Создание поля ввода для параметра K
input_label = tk.Label(input_frame, text="Введите K:")
input_label.pack(side=tk.LEFT)
input_entry = tk.Entry(input_frame)
input_entry.pack(side=tk.LEFT)

# Создание окна вывода максимальной суммы
max_sum_frame = tk.Frame(root)
max_sum_frame.pack(pady=10)

max_sum_label = tk.Label(max_sum_frame, text="Максимальная сумма по модулю 8: ")
max_sum_label.pack()

# Создание кнопки для запуска программы
run_button = tk.Button(root, text="Запустить", command=run_program)
run_button.pack()

# Создание текстового поля для вывода результатов
result_text = scrolledtext.ScrolledText(root, width=60, height=20)
result_text.pack()

root.mainloop()
