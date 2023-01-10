import sys
# Библиотека, которая упрощает относительные импорты файлов и модулей
from pyhere import here

# Добавляем фолдер 1_week в Path, чтобы импортировать оттуда функцию add
sys.path.append(str(here("1_week").resolve()))
from test_file1 import add


def test_add_positive():
    assert add(2, 2) == 4


def test_add_negative():
    assert add(-2, -4) == - 6
