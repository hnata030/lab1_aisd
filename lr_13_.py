'''
30.	Определить суммарную стоимость билетов взрослых(=>18)
на борту в возрастном интервале мода +- 5 позиций
'''
""""
напиши на питоне на основе кода, представленного ниже и убери иp кода определение количества взрослых на борту в возрастном 
интервале медиана +- 5 позиций и сколько из них выжило, вместо этого напиши туда задание представленное ниже.
Задание: Определить суммарную стоимость билетов взрослых(=>18)
на борту в возрастном интервале мода +- 5 позиций.

import csv
# Открываем файл
with open('titanic.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    adult_count = 0
    survived_count = 0

    adult_ages = []

 
    for row in csv_reader:
        age = row[5]
        if age.isdigit():
            age = int(age)
             # Проверяем, является ли пассажир взрослым
            if age >= 18:
                adult_count += 1
                adult_ages.append(age)
                # Проверяем, выжил ли пассажир
                if int(row[1]) == 1:
                    survived_count += 1

    # Сортируем массив возрастов взрослых пассажиров
    adult_ages.sort()

    # Вычисляем медиану возрастов взрослых пассажиров
    median = adult_ages[len(adult_ages) // 2]

    # Определяем диапазон возрастов, включающий медиану +/- 5 позиций
    age_start = median - 5
    age_end = median + 5

    # Выводим результаты
    print("Количество взрослых пассажиров в заданном возрастном интервале:", adult_count)
    print("Количество выживших взрослых пассажиров в заданном возрастном интервале:", survived_count)
    print("Медиана возрастов взрослых пассажиров:", median)
    print("Диапазон возрастов, включающий медиану +/- 5 позиций:", age_start, "-", age_end)
"""
import csv

# Открываем файл
with open('titanic.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    adult_ticket_cost = 0
    adult_ages = []
    mode_age = 0
    for row in csv_reader:
        age = row[5]
        if age.isdigit():
            age = int(age)
            if age >= 18:
                
                # Проверяем, входит ли возраст в модальный интервал
                if mode_age - 5 <= age <= mode_age + 5:
                    adult_ticket_cost += float(row[9])
                adult_ages.append(age)
    adult_ages.sort()

    # Вычисляем моду возрастов взрослых пассажиров
    mode_age = max(set(adult_ages), key=adult_ages.count)
    
    # Определяем диапазон возрастов, включающий моду +/- 5 позиций
    age_start = mode_age - 5
    age_end = mode_age + 5
    
    # Вывод
    print("Суммарная стоимость билетов взрослых пассажиров в заданном возрастном интервале:", adult_ticket_cost)

























    
