__author__ = "Высоцкая И.Д."
'Модуль с функциями'

"""Функция, высчитывающая факториал
n - число, факториал которого нужно вычислить
Возвращает целое число"""
def fact(n):
    if n < 0:
        return "Число меньше 0"
    if n == 0:
        return 1
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

"""Функция, высчитывающая сумму
n - размер списка, arr - список из элементов типа float
Возвращает результат вычислений типа float"""
def summ(n: int, arr: list[float])-> float:
    s = 0.0
    for i in range(0, n):
        s += arr[i]/fact(i)
    return s