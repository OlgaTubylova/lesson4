# Напишите функцию для транспонирования матрицы
# Транспонирование матрицы — это операция, при которой строки матрицы становятся столбцами, а столбцы — строками.

import numpy as np

# 1. Использование списковых включений (List Comprehension)
def transpose_list_comprehension(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# 2. Использование функции zip()
def transpose_zip(matrix):
    return list(map(list, zip(*matrix)))


# 3. Использование библиотеки NumPy
def transpose_numpy(matrix):
    return np.transpose(matrix).tolist()


matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]]
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]

print(transpose_list_comprehension(matrix))
print(transpose_zip(matrix))
print(transpose_numpy(matrix))
