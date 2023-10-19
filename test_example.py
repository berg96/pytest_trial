import pytest


def one_more(x):
    return x + 1


def test_correct():
    print('Правильный тест')  # Новая строка.
    assert one_more(4) == 5


def test_fail():
    print('Неправильный тест')  # Новая строка.
    assert one_more(3) == 5


def division(dividend, divisor):
    return dividend / divisor


@pytest.mark.skip
def test_zero_division():
    with pytest.raises(ZeroDivisionError):  # Ожидается ошибка деления на 0.
        # При вызове функции с такими аргументами возникнет ошибка.
        result = division(1, 0)


def get_sort_list(string):
    new_list = sorted(string.split(', '))
    return new_list


def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']


def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    # Провальный тест:
    # ожидаем число, но вернётся список.
    assert isinstance(result, int)
