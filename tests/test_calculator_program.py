import pytest
from calculate.calculator_program import calculate


def test_calculate_addition():
    assert calculate(1, 1, '+') == 2


def test_calculate_subtraction():
    assert calculate(5, 3, '-') == 2


def test_calculate_multiplication():
    assert calculate(4, 3, '*') == 12


def test_calculate_division():
    assert calculate(8, 2, '/') == 4


def test_calculate_division_by_zero():
    assert calculate(5, 0, '/') == "Ошибка: Деление на ноль."



def test_calculate_large_numbers():
    assert calculate(1000000, 1000000, '+') == 2000000


def test_calculate_negative_numbers():
    assert calculate(-5, -3, '+') == -8


def test_calculate_fractional_numbers():
    assert calculate(2.5, 4.3, '+') == 6.8


def test_calculate_zero_operation():
    assert calculate(0, 0, '+') == 0
    assert calculate(0, 0, '-') == 0
    assert calculate(0, 0, '*') == 0

'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
