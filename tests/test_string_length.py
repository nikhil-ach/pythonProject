import pytest
import string_length

@pytest.mark.parametrize("my_list, count", [
    (['abc', 'xyz', 'aba', '1221'], 2),
    (['efd', 'fgf', 'gas', 'efd'], 1),
    (['iai', 'jas', '121', '4564'], 3)
])

def test_list(my_list, count):
    assert string_length.stringLength(my_list) == count