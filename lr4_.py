"""
Формируется матрица F следующим образом: скопировать в нее А и  если в С количество нулей в нечетных столбцах и четных строках больше,
чем произведение чисел по периметру, то поменять местами В и С симметрично,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A-1*AT – K * FТ,
иначе вычисляется выражение (AT +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import random
import time
import numpy as np
from matplotlib import pyplot as plt
N = int(input('Введите длину матрицы(положительное, целое число, > 3)): '))
while N <= 3:
    N = int(input('Введите длину матрицы(положительное, целое число, > 3)): '))
K = int(input('Введите число K(целое число): '))
start = time.monotonic()
np.set_printoptions(linewidth=1000)
#создание и заполнение матрицы А
A = np.random.randint(-10.0, 10.0, (N, N))
print('Матрица А:\n', A)
#создание подматриц
submatrix_length = N // 2
sub_matrix_B = np.array(A[:submatrix_length, :submatrix_length])
sub_matrix_C = np.array(A[:submatrix_length, submatrix_length+N % 2:N])
sub_matrix_D = np.array(A[submatrix_length:, :submatrix_length])
sub_matrix_E = np.array(A[submatrix_length+N % 2:N, submatrix_length+N % 2:N])
#создание матрицы F
F = A.copy()
print('\n Матрица F: \n', F)
#Обработка матрицы C
count_number_in_column = np.sum(sub_matrix_B[:, 0:submatrix_length % 2])
count_number_in_line = np.sum(sub_matrix_B[0:submatrix_length // 2, :])
perimeter_product = np.prod(np.concatenate([A[0, :], A[1:-1, -1], A[-1, ::-1], A[1:-1, 0][::-1]]))
#формируем матрицу F
if (count_number_in_column) and (count_number_in_line) > perimeter_product:
    
    F[:submatrix_length, :submatrix_length] = sub_matrix_C[:submatrix_length, ::-1]
    F[:submatrix_length, submatrix_length + N % 2:N] = sub_matrix_B[:submatrix_length, ::-1]
else:
    F[:submatrix_length, :submatrix_length] = sub_matrix_C
    F[:submatrix_length, submatrix_length + N % 2:N] = sub_matrix_B
    
print('\n Отформатированная матрица F: \n', F)
#вычисляем выражение
try:
    if np.linalg.det(A) > sum(np.diagonal(F)):
        print('Результат выражения A^(-1)*A^T–K*F^Т:\n', np.linalg.inv(A) * A.transpose() - K * F.transpose())
    else:
        G = np.tri(N)*A
        print('\n Результат выражения (А^T+G-F^(-1)*K): \n', (A.transpose() + G - np.linalg.inv(F)) * K)
except np.linalg.LinAlgError:
    print('Одна из матриц является вырожденной (определитель равен 0), поэтому обратную матрицу найти невозможно')
finish = time.monotonic()
print('\n Время работы программы: ', finish - start, ' sec.')
print('\n Матрица, которая используется при построении графиков:\n', A)
#использование библиотеки matplotlib
av = [np.mean(abs(A[i, ::])) for i in range(N)]
av = int(sum(av))
fig, axs = plt.subplots(2, 2, figsize=(11, 8))
x = list(range(1, N+1))
for j in range(N):
    y = list(A[j, ::])
    #Программа выводит обычный график
    axs[0, 0].plot(x, y, label=f"{j} строка.")
    axs[0, 0].set(title='График с использованием функции plot:', xlabel='Номер элемента в строке', ylabel='Значение элемента')
    axs[0, 0].grid()
    #программа выводит гистограмму, по которой можно определить min и max n-ый элемент среди всех
    axs[0, 1].bar(x, y, 0.4, label=f'{j} строка.')
    axs[0, 1].set(title='График с использование функции  bar:', xlabel='Номер элемента в строке', ylabel='Значение элемента')
    if N <= 10:
        axs[0, 0].legend(loc='lower right')
        axs[0, 1].legend(loc='lower right')
    #Программа выводит среднее значение от каждой строки
    explode = [0]*(N-1)
    explode.append(0.1)
    sizes = [round((np.mean(abs(A[i, ::])) + 100)/av, 1) for i in range(N)]
    axs[1, 0].set_title('График с использованием функции pie:')
    axs[1, 0].pie(sizes, labels=list(range(1, N+1)), explode=explode, autopct='%1.1f%%', shadow=True)
    plt.suptitle('Использование библиотеки matplotlib')
    plt.tight_layout()
    plt.show()
