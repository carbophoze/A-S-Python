# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
import random

SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = 1

numbers = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(f'Before {numbers}')
i_min = i_max = 0

for i, value in enumerate(numbers):
    if value < numbers[i_min]:
        i_min = i
    elif value > numbers[i_max]:
        i_max = i

numbers[i_min], numbers[i_max] = numbers[i_max], numbers[i_min]
print(f'After  {numbers}')
print(f'Reversing values №{i_min} and №{i_max}')
