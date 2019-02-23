#  https://drive.google.com/file/d/1He3VexXkymlpKqmRFmlE9vTKPy7pP8qK/view?usp=sharing

#  Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
#  Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def dTimes(s, x):
    d = 0
    for n in s:
        if n == x:
            d += 1
    return d


def doIt(n, x):
    s = input('Введите число: ')
    if n > 1:
        doIt(n-1, x)
    if dTimes(s, x) > 0:
        print(f'Число вхождений {x} в {s} = {dTimes(s, x)} раз(а)')


n = int(input('Введите кол-во чисел: '))
x = input('Введите цифру для поиска: ')
doIt(n, x)
