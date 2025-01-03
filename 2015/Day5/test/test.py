import pytest

import source.solution as solution

@pytest.fixture
def testable_NONS():
    """Simple fixture to that will pass all three requirments in part one"""
    return solution.Naughty_Or_Nice_Text("faaart")

def test_class_attributes(testable_NONS):
    """Ensuring that the class takes only one parameter and it's a string"""
    assert hasattr(testable_NONS, "text")
    assert isinstance(testable_NONS.text, str)

@pytest.mark.parametrize("test_input,expected", [
    ("faaart", True),
    ("fooort", True),
    ("faeirt", True),
    ("frrt", False)
])
def test_vowels_check(test_input, expected):
    """test to ensure it will return the correct response for what vowels are counted"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.three_vowel_check() == expected

@pytest.mark.parametrize("test_input,expected",[
    ("passes", True),
    ("grabbed", False)
])
def test_banned_combos_check(test_input, expected):
    """banned combos are checked against the text"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.banned_combos_check() == expected

@pytest.mark.parametrize("test_input,expected",[
    ("passed", True),
    ("fail", False)
])
def test_consecutive_letters_check(test_input, expected):
    """needs at least two consecutive letters to pass"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.consecutive_letters_check() == expected

@pytest.mark.parametrize("test_input,expected", [
    ("Tarrasque", True),
    ("Queue", False)
])
def test_passed_all_part_one_checks(test_input,expected):
    """Checks if the three checks for part one are passed"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.passed_all_part_one_checks() == expected

@pytest.mark.parametrize("test_input,expected", [
    ("xx", False),
    ("xxx", False),
    ("xxxx", True),
    ("xxyxx", True),
    ("xxxyxx", True),
    ("cgycg", True),
    ("CGCG", True)
])
def test_double_consecutive_letters_check(test_input,expected):
    """testing if there are any double sets of letters that must no overlap"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.double_consecutive_letters_check() == expected

@pytest.mark.parametrize("test_input,expected", [
    ("xyx", True),
    ("xxy", False),
    ("xxx", True)
])
def test_repeat_pattern_check(test_input,expected):
    """three most simple versions of the pattern tested against the regex"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.repeat_pattern_check() == expected

@pytest.mark.parametrize("test_input,expected", [
    ("xxyxx", True),
    ("xxxxxyx", True),
    ("googlegoo", False)
])
def test_passed_all_part_two_checks(test_input,expected):
    """Checks if the two checks for part twp are passed"""
    testing = solution.Naughty_Or_Nice_Text(test_input)
    assert testing.passed_all_part_two_checks() == expected


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

def test_main(mocker):
    """Test of the  main loop"""
    mock_file_data_as_list = """Tarrasque, Queue"""
    mocked_open = mocker.patch("builtins.open", mocker.mock_open(read_data=mock_file_data_as_list))
    result = solution.intake_values("dummy_file.txt")
    assert result ==mock_file_data_as_list.splitlines(keepends=True)
    assert solution.main() == 1