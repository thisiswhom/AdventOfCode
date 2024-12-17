import pytest

import source.solution as solution

#test for direction

def test_up_direction():
    result = solution.direction("(")
    assert result == 1

def test_down_direction():
    result = solution.direction(")")
    assert result == -1

def test_incorrect_symbol_direction():
    with pytest.raises(ValueError, match="Unsupported symbol:"):
        solution.direction("$")

# tests for floor_calculation_loop

def test_equal_0_floor_calculation_loop():
    result = solution.floor_calculation_loop("(())")
    assert result == 0

def test_equal_neg_onefloor_calculation_loop():
    result = solution.floor_calculation_loop("(()))")
    assert  result == -1

def test_equal_pos_onefloor_calculation_loop():
    result = solution.floor_calculation_loop("(((()))")
    assert  result == 1

# test for find_first_negative

def test_find_first_negative():
    result = solution.find_first_negative("(()))((")
    assert result == 5




