import pytest
import range_7div

@pytest.mark.parametrize("input, if_range", [
    (1000, False),
    (2030,  True),
    (3500,  False)
])
def test_range_7div(input, if_range):
    assert range_7div.check_range(input) == (if_range)

@pytest.mark.parametrize("input_1, if_range_1", [
    (2065, False),
    (2009,  True),
    (2043,  False)
])
def test_range_7div(input_1, if_range_1):
    assert range_7div.check_div(input_1) == (if_range_1)

