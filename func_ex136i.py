__author__ = "Высоцкая И.Д."
'Модуль с функциями, факториал оптимизировать'

def fact(prev, n):
    """
    Функция, вычисляющая факториал
    prev — предыдущий факториал ((n-1)!), n — текущее число
    Возвращает целое число
    """
    return prev * n


def summ(arr):
    """
    Функция, вычисляющая сумму a1/0! + a2/1! + ... + an/(n-1)!
    arr — список чисел [a1, a2, ..., an]
    Возвращает результат типа float
    """
    if not arr:
        return 0.0

    total = 0.0
    prev_fact = 1

    for i in range(len(arr)):
        if i > 0:
            prev_fact = fact(prev_fact, i)

        total += arr[i] / prev_fact # добавляем следующий член суммы: a[i] / i!
    return total