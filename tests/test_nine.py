import pytest
import nine

@pytest.mark.parametrize("letters, output", [
    (['a', 'b', 'c', 'd'], 'a, 1\nb, 2\nc, 3\nd, 4'),

])

def test_list(letters, output):
    assert nine.nine_1(letters) == output