"""
31.Формируется матрица F следующим образом: если в С количество нулей в нечетных столбцах и четных строках в области 3 больше,
чем произведение чисел по периметру области 2, то поменять в С симметрично области 1 и 3 местами,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: (К*A )*А-K* F T .
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
from math import sqrt, ceil, modf 
from random import randint 
 
 
def pretty_print(matrix, n): 
    for i in range(n): 
        print(matrix[i]) 
 
 
def random_matrix_generation(n): 
    for i in range(n ** 2): 
        matrix.append(randint(-10, 10)) 
 
 
def symmetrically(): 
    print("Симметрично меняем области 1 и 3 в C") 
    pretty_print(C, submatrix_size) 
    for i in range(submatrix_size): 
        for j in range(submatrix_size): 
            if i >= j and i <= submatrix_size - 1 - j: 
                C[i][j], C[i][submatrix_size - (j + 1)] = C[i][submatrix_size - (j + 1)], C[i][j] 
    print("|") 
    print("|") 
    print("V") 
    pretty_print(C, submatrix_size) 
 
 
def matrix_multiply(first_matrix, second_matrix): 
    print("Умножаем матрицу") 
    pretty_print(first_matrix, len(first_matrix)) 
    print("на") 
    pretty_print(second_matrix, len(second_matrix)) 
 
    result_matrix = [[0 for i in range(N)] for i in range(N)] 
    for i in range(N): 
        for j in range(N): 
            for k in range(N): 
                result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j] 
 
    print("Получаем") 
    pretty_print(result_matrix, len(result_matrix)) 
    return result_matrix 
 
 
def matrix_subtraction(first_matrix, second_matrix): 
    print("Вычитаем из матрицы") 
    pretty_print(first_matrix, len(first_matrix)) 
    print("матрицу") 
    pretty_print(second_matrix, len(second_matrix)) 
 
    result_matrix = [[0 for i in range(N)] for i in range(N)] 
    for i in range(N): 
        for j in range(N): 
            result_matrix[i][j] = first_matrix[i][j] - second_matrix[i][j] 
 
    print("Получаем") 
    pretty_print(result_matrix, len(result_matrix)) 
    return result_matrix 
 
 
def transpose(matrix): 
    print("Транспонируем матрицу") 
    pretty_print(matrix, len(matrix)) 
    res = list() 
    for j in range(N): 
        tmp = list() 
        for i in range(N): 
            tmp = tmp + [matrix[i][j]] 
        res = res + [tmp] 
    return res 
 
 
matrix = list() 
B = list() 
C = list() 
D = list() 
E = list() 
F = list() 
K_matrix = list() 
 
N = int(input("Введите N: ")) 
K = int(input("Введите K: ")) 
for i in range(N): 
    for j in range(N): 
        if i == j: 
            K_matrix.append(K) 
        else: 
            K_matrix.append(0) 
 
random_matrix_generation(N) 
t = sqrt((N * N) / 4) 
submatrix_size = ceil(t) 
A = [matrix[i * N:(i + 1) * N] for i in range(N)] 
K = [K_matrix[i * N:(i + 1) * N] for i in range(N)] 
 
print("Матрица A") 
pretty_print(A, N) 
# Разбиваем матрицу на 4 подматрицы 
if modf(t)[0] == 0: 
    B = [[A[i][j] for i in range(submatrix_size) for j in range(submatrix_size)][ 
         i * submatrix_size:(i + 1) * submatrix_size] for i in range(submatrix_size)] 
    C = [[A[i][j] for i in range(submatrix_size) for j in range(submatrix_size, N)][ 
         i * submatrix_size:(i + 1) * submatrix_size] for i in range(submatrix_size)] 
 
    D = [[A[i][j] for i in range(submatrix_size, N) for j in range(submatrix_size)][ 
         i * submatrix_size:(i + 1) * submatrix_size] for i in range(submatrix_size)] 
 
    E = [[A[i][j] for i in range(submatrix_size, N) for j in range(submatrix_size, N)][ 
         i * submatrix_size:(i + 1) * submatrix_size] for i in range(submatrix_size)] 
else: 
    B = [[A[i][j] for i in range(submatrix_size) for j in range(submatrix_size)][ 
         i * submatrix_size:(i + 1) * submatrix_size] for i in range(submatrix_size)] 
    C = [[A[i][j] for i in range(submatrix_size) for j in range(submatrix_size - 1, N)][ 
         i * submatrix_size:(i + 1) * submatrix_size] for i in range(submatrix_size)] 
 
    D = [[A[i][j] for i in range(submatrix_size - 1, N) for j in range(submatrix_size)][ 
         i * submatrix_size:(i + 1) * submatrix_size] for i in range(submatrix_size)] 
 
    E = [[A[i][j] for i in range(submatrix_size - 1, N) for j in range(submatrix_size - 1, N)][ 
         i * submatrix_size:(i + 1) * submatrix_size] for i in range(submatrix_size)] 
 
# Считаем кол-во нулей и произв. периметра 
count_zero = 0
perimeter_product = 1 
for i in range(submatrix_size): 
    for j in range(submatrix_size): 
        if i <= j and i >= submatrix_size - 1 - j: 
            if i % 2 != 0 and j % 2 == 0 and C[i][j] == 0: 
                count_zero += 1 
        if i <= j and i <= submatrix_size - 1 - j: 
            if i == 0 or j == 0 or i == j or i + j == submatrix_size - 1: 
                perimeter_product *= C[i][j] 
print("Количество нулей в нечетных столбцах и четных строках в области 3 = " + str(count_zero)) 
print("Произведение чисел по периметру области 2 = " + str(perimeter_product)) 
if count_zero > perimeter_product: 
    symmetrically() 
else: 
    C, E = E, C 
    print("Несимметрично поменяли C и E") 
 
# Формируем матрицу F 
for i in range(submatrix_size): 
    if modf(t)[0] != 0: 
        B[i].pop() 
        D[i].pop() 
    for j in range(submatrix_size): 
        B[i].append(C[i][j]) 
        D[i].append(E[i][j]) 
if modf(t)[0] != 0: 
    B.pop(submatrix_size - 1) 
F = B + D 
print("Матрица F") 
pretty_print(F, N) 
result = matrix_subtraction(matrix_multiply(matrix_multiply(K, A), A), matrix_multiply(K, transpose(F))) 
print("Результат вычислений") 
pretty_print(result, N)
