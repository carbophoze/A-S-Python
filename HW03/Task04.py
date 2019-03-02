# Определить, какое число в массиве встречается чаще всего.

import random
SIZE = 10
MAX_LIMIT = 5
MIN_LIMIT = 1

numbers = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
numbers_frequency = [0 for _ in range(MIN_LIMIT, MAX_LIMIT + 1)]

print(numbers)
for n in numbers:
    numbers_frequency[n - MIN_LIMIT] += 1

print()
for i, value in enumerate(numbers_frequency):
    print(f' №{i + MIN_LIMIT:3} | Value = {value}')
