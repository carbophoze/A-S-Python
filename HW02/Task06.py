#  Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#  Вывести на экран это число и сумму его цифр.


def xSum(n):
    if n > 9:
        return n % 10 + xSum(n // 10)
    else:
        return n


def fn():
    x = int(input('Введите натуральное число(0-окончание ввода): '))
    if x == 0:
        xm = 0
    else:
        xm = fn()
        if xSum(x) >= xSum(xm):
            xm = x
    return xm


maxNum = fn()
sumMaxNum = xSum(maxNum)
print(f'Число с большей суммой цифр {maxNum}. Сумма = {sumMaxNum}')

