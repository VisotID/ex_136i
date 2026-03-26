__author__ = "Высоцкая И.Д."
'Модуль с тестами'

from func_ex136i import * # подключаем модуль с функциями
import pytest

def test():
    """Функция с тестами"""
    assert summ([1,2,3,4,5]) == pytest.approx(5.375, abs=0.00001)
    assert summ([1.3, 1.2, 1.2]) == pytest.approx(3.1, abs=0.00001)
    assert summ([-1.2, 1, -10]) == pytest.approx(-5.2, abs=0.00001)
    assert summ([2,7,8]) == 13.0
    assert summ([11,0] ) == 11.0