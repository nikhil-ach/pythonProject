import unittest
import pytest
import positive_int


@pytest.mark.parametrize("input, output", [
    ([1,0,3,-3,-4], [1,0,3]),
    ([], []),
    ([3,6,7,9], [3,6,7,9]),
    ([-1,-2,-3],[])
])
def test_positive_int(input, output):
    assert positive_int.remove_negative(input) == (output)