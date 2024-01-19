import pytest
import square_dict

@pytest.mark.parametrize("input_1, output_1", [
    (8, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}),
    (-3,  {}),
    (0,  {})
])

def test_square_dict(input_1, output_1):
    assert square_dict.square_dict(input_1) == (output_1)