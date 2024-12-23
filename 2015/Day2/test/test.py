import pytest
import source.solution as solution

@pytest.fixture
def testable_rpp():
    return solution.Rectangular_Prism_Present(2,4,3)

@pytest.fixture
def sample_string():
    return "2x3x4"

mock_file_data = """2x3x4
1x2x3
"""

def test_RPP_attributes(testable_rpp):
        #rpp = solution.Rectangular_Prism_Present()
        assert hasattr(testable_rpp, "length")
        assert hasattr(testable_rpp, "width")
        assert hasattr(testable_rpp, "height")
        assert hasattr(testable_rpp, "lxw")
        assert hasattr(testable_rpp, "lxh")
        assert hasattr(testable_rpp, "hxw")

def test_RPP_surface_area(testable_rpp):
    assert testable_rpp.surface_area() == ((2*3)*2) + ((2*4)*2) + ((4*3)*2)

def test_RPP_smallest_side(testable_rpp):
    assert testable_rpp.smallest_side() == 6

def test_wrapping_paper_needed(testable_rpp):
    assert testable_rpp.wrapping_paper_needed() == 58

def test_ribbon_wrap(testable_rpp):
    assert testable_rpp.ribbon_wrap() == 2+2+3+3 == 10

def test_ribbon_bow(testable_rpp):
    assert testable_rpp.ribbon_bow() == 2*3*4 == 24

def test_ribbon_needed(testable_rpp):
    assert testable_rpp.ribbon_needed() == (2*3*4) + (2+2+3+3) == 34


def test_intake_presents(mocker):
    """Simulates opening a file using the pytest-mock plugin

    It's really cool how it says 'for this test, when you see the open fucntion
     called, intercept it and instead return this other file"""
    mocked_open = mocker.patch("builtins.open", mocker.mock_open(read_data=mock_file_data))
    result = solution.intake_presents("dummy_file.txt")
    assert result ==mock_file_data.splitlines(keepends=True)

def test_convert_present_string_to_ints(sample_string):
    assert solution.convert_present_string_to_ints(sample_string) == [2,3,4]

def test_create_file_path(mocker):
    """Another cool use of mocker to mock os functions and return my chosen values """
    mock_current_dir = "/mocked/directory"
    mocker.patch("os.path.dirname", return_value=mock_current_dir)
    mocker.patch("os.path.abspath", return_value=mock_current_dir)
    result = solution.create_file_path("values")
    assert result == "/mocked/directory/values"


def test_main():
    solution.main()