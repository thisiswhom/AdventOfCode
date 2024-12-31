import pytest, re

import source.solution as solution

@pytest.mark.parametrize("test_input,expected", [
    ("abcdef609043", "000001dbbfa3a5c83a2d506429c7b00e"),
])
def test_get_md5_of_string(test_input, expected):
    """
    testing my md5 hash generator agaisnt the test values given in the example
    """
    assert solution.get_md5_of_string(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("000001dbbfa3a5c83a2d506429c7b00e", True),
    ("0000112312300000", False)
])
def test_use_regex(test_input,expected):
    """
    confirms that the funciton will only return True if the first five
    characters are "0"
    """
    assert solution.use_regex(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("pqrstuv", 1048970)
])
def test_find_lowest_number(test_input,expected):
    """

    :param test_input:
    :param expected:
    :return:
    """
    assert solution.find_lowest_number(test_input) == expected