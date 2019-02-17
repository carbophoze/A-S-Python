#  Ссылка на блок-схемы
#  https://drive.google.com/file/d/1_NGQTXeukAkAp3l1uBkRPfkKoD0XPRcL/view?usp=sharing


#  Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите целое положительное трехзначное число: '))

s = x % 10
m = s

x //= 10
s += x % 10
m *= x % 10

x //= 10
s += x % 10
m *= x % 10

print(f'Сумма цифр: {s}')
print(f'Произведение цифр: {m}')
