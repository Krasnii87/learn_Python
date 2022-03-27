# 1. Разложить положительные и отрицательные числа по разным массивам

# import random
#
# array = [random.randint(-100, 100) for _ in range(100)]
# print(array)
#
# arr_below = []
# arr_lager = []
#
# for item in array:
#
#     if item > 0:
#         arr_lager.append(item)
#     elif item < 0:
#         arr_below.append(item)
#
# print(arr_below)
# print(arr_lager)

# 2. Вставка элемента в произвольное мессто массива

import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите целое число для вставки: '))
pos = int(input('На каакую позицию вставить число: '))

# array.append(None)
# i = len(array) - 1
#
# while i > pos:
#     array[i], array[i - 1] = array[i - 1], array[i]
#     i -= 1

array.insert(pos, num)

array[pos] = num
print(array)