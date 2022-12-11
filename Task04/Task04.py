# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random

k = int(input("Введите коэффициент: "))

res = ''
for i in range(k):
    koef = random.randint(0, 100)
    if koef == 1:
        if k - i > 1:
            res += 'x^' + str(k - i)
        else:
            res += 'x'
    if koef > 1:
        if k - i > 1:
            res += str(koef) + '*x^' + str(k - i)
        else:
            res += str(koef) + '*x'
    if i != k - 1:
        res += '+'

print(res)