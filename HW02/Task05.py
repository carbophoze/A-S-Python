# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
import sys

sys.setrecursionlimit(5000)

def fn(n):
    if n == 0:
        return 0
    return n + fn(n-1)


n = int(input('Введите натуральное число: '))
left = fn(n)
right = n*(n+1)/2

if left == right:
    print(f'Формула верная. {left} = {int(right)}')
else:
    print(f'Формула неверная. {left} != {right}')
