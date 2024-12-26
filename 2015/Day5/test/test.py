import pytest

import source.solution as solution

@pytest.fixture
def testable_NONS():
    """Simple fixture to that will pass all three requirments in part one"""
    return solution.Naughty_Or_Nice_Text("faaart")

def test_NONS_attributes(testable_NONS):
    """Ensuring that the class takes only one parameter and its a string"""
    assert hasattr(testable_NONS, "text")
    assert isinstance("text", str)

@pytest.mark.parametrize("test_input,expected", [("faaart", True), ("fooort", True),("faeirt", True), ("frrt", False)])
def test_NONS_vowels(test_input, expected):
    """test to ensure it will return the correct response for what vowels are counted"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.three_vowel_check() == expected


@pytest.mark.parametrize("test_input,expected",[("passes", True)])
def test_NONS_no_no_list(test_input, expected):
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.no_no_list() == expected



