# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


answer = [list() for _ in range(8)]

for i_number in range(2, 100):
    for k_number in range(2, 10):
        if i_number % k_number == 0:
            answer[k_number-2].append(i_number)

for n, k_number in enumerate(answer):
    print(f'Числа, кратные {n+2}: {k_number}')


