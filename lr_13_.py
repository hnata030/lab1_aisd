'''
Определить суммарную стоимость билетов детей(<18)  на борту в возрастном интервале мода +- 6 позиций 
'''

import csv

# ОТкрываем файл
with open('titanic.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    adult_ticket_cost = 0
    adult_count = 0
    survived_count = 0
    
    adult_ages = []
    mode_age = 0
    
    for row in csv_reader:
        age = row[5]
        if age.isdigit():
            age = int(age)
            # Проверяем, является ли пассажир ребенком
            if age < 18:
                adult_count += 1
                adult_ages.append(age)
                
                # Проверяем, входит ли возраст в модальный интервал
                if mode_age - 6 < age < mode_age + 6:
                    adult_ticket_cost += float(row[9])
                adult_ages.append(age)
                
    adult_ages.sort()
    
    # Вычисляем моду возрастов детей
    mode_age = max(set(adult_ages), key=adult_ages.count)
    
    # Определяем диапазон возрастов, включающий моду +/- 6 позиций
    age_start = mode_age - 6
    age_end = mode_age + 6

    # Вывод
    print("Количество детей в заданном возрастном интервале:", adult_count)
    print("Суммарная стоимость билетов пассажиров в заданном возрастном интервале:", adult_ticket_cost)
    print("Мода возрастов пассажиров:", mode_age)
    print("Диапазон возрастов, включающий моду +/- 6 позиций:", age_start, "-", age_end)
