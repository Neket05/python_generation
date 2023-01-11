from typing import List, Tuple


def int_to_string(number: int) -> str:
    """Take int value and return a stringified value"""
    raise NotImplementedError


def find_unique_elements_in_list(array: list) -> list:
    """Take an array of values and returns an array of unique elements."""
    raise NotImplementedError


def drop_index_column(columns: List[str]) -> List[str]:
    """Take an array of string values, if 'index' is found, drop it. Return an array of string values."""
    raise NotImplementedError


def sum_elements(array: List[int]) -> int:
    """Take an array of integers and return the sum of all elements."""
    raise NotImplementedError


def is_gps_available(columns: Tuple[str]) -> bool:
    """Take a tuple of string values and check if 'Lat' and 'Lon' are elements of the tuple"""
    raise NotImplementedError


def test_int_to_string():
    assert int_to_string(1) == "1"


def test_find_unique_elements_in_list():
    assert find_unique_elements_in_list([1, 1, 1, 1, 1, 2, 10000]) == [1, 2, 10000]
    assert find_unique_elements_in_list([]) == []


def test_drop_index_column():
    assert drop_index_column(["index"]) == []
    assert drop_index_column(["index", "first", "secondd"]) == ["first", "second"]
    assert drop_index_column([]) == []


def test_sum_elements():
    assert sum_elements([]) == 0
    assert sum_elements([1, 100, 10000]) == 10101
    assert sum_elements([-1, -100, -10000]) == 10101


def test_is_gps_available():
    assert not is_gps_available(("a", "b"))
    assert not is_gps_available(("Lat", "b"))
    assert not is_gps_available(("Lon", "c", "a"))
    assert is_gps_available(("Lat", "Lon"))
    assert is_gps_available(("1", "foo", "Lat", "bar", "Lon"))
