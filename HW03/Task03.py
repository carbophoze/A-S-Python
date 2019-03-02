# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random

SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = 1

source_tuple = tuple(random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE))

print(f'Исходные данные {source_tuple}')
answer = list()
for i, value in enumerate(source_tuple):
    if value % 2 == 0:
        answer.append(i)

print(f'Список индексов четных элементов: {answer}')
for n in answer:
    print(f'Элемент №{n} Значение {source_tuple[n]}')
