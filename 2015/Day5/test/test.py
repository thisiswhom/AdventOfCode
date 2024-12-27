import pytest

import source.solution as solution

@pytest.fixture
def testable_NONS():
    """Simple fixture to that will pass all three requirments in part one"""
    return solution.Naughty_Or_Nice_Text("faaart")

def test_NONS_attributes(testable_NONS):
    """Ensuring that the class takes only one parameter and its a string"""
    assert hasattr(testable_NONS, "text")
    assert isinstance(testable_NONS.text, str)

@pytest.mark.parametrize("test_input,expected", [("faaart", True), ("fooort", True),("faeirt", True), ("frrt", False)])
def test_NONS_vowels_check(test_input, expected):
    """test to ensure it will return the correct response for what vowels are counted"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.three_vowel_check() == expected

@pytest.mark.parametrize("test_input,expected",[("passes", True), ("grabbed", False)])
def test_NONS_banned_combos_check(test_input, expected):
    """"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.banned_combos_check() == expected

@pytest.mark.parametrize("test_input,expected",[("passed", True), ("fail", False)])
def test_NONS_consecutive_letters_check(test_input, expected):
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.consecutive_letters_check() == expected

@pytest.mark.parametrize("test_input,expected", [("Tarrasque", True), ("Queue", False)])
def test_NONS_passed_all_tests(test_input,expected):
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.passed_all_tests() == expected



def test_intake_vales(mocker):
    """Simulates opening a file using the pytest-mock plugin"""
    mock_file_data_as_list = """mdskbvzguxvieilr, anjcvqpavhdloaqh"""
    mocked_open = mocker.patch("builtins.open", mocker.mock_open(read_data=mock_file_data_as_list))
    result = solution.intake_values("dummy_file.txt")
    assert result ==mock_file_data_as_list.splitlines(keepends=True)

def test_create_file_path(mocker):
    """use of mocker to mock os functions and return my chosen values """
    mock_current_dir = "/mocked/directory"
    mocker.patch("os.path.dirname", return_value=mock_current_dir)
    mocker.patch("os.path.abspath", return_value=mock_current_dir)
    result = solution.create_file_path("values")
    assert result == "/mocked/directory/values"

def test_main():
    assert solution.main()