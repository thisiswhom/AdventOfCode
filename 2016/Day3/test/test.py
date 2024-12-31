import pytest

import source.solution as solution

@pytest.mark.parametrize("side_a, side_b, side_c,expected", [
    (1,1,1, True),
    (5,10,25, False)
])
def test_triangle_checker(side_a, side_b, side_c, expected):
    result = solution.triangle_checker(side_a, side_b, side_c)
    assert result == expected

import pytest

def test_reorder_triangle_list_vertically():
    input_data = [
        "101 301 501",
        "102 302 502",
        "103 303 503",
        "201 401 601",
        "202 402 602",
        "203 403 603"
    ]
    expected_output = [
        [101, 102, 103], [201, 202, 203],  # Column 1 triangles
        [301, 302, 303], [401, 402, 403],  # Column 2 triangles
        [501, 502, 503], [601, 602, 603]   # Column 3 triangles
    ]
    result = solution.reorder_triangle_list_vertically(input_data)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


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