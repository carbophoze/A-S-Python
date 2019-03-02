# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться
import random

SIZE = 10
MAX_LIMIT = 9
MIN_LIMIT = 1

source = tuple(random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE))
# source = (5, 8, 9, 4, 7, 9, 9, 9, 9, 9)
print(source)

n1_min = 0
n2_min = 1
for n in range(2, SIZE):
    value = source[n]
    if value < source[n1_min]:
        n1_min = n
    elif value < source[n2_min]:
        n2_min = n

print(f'Наименьший элемент 1: №{n1_min}  Value: {source[n1_min]}')
print(f'Наименьший элемент 2: №{n2_min}  Value: {source[n2_min]}')

