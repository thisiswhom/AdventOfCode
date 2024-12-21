import pytest

import source.solution as solution

@pytest.fixture
def testable_rpp():
    return solution.Rectangular_Prism_Present(2,3,4)

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

def test_RPP_smallest_side(testatble_rpp):
    pass