import pytest
import zip

@pytest.mark.parametrize("combined, output", [
    (([1,2,3,4],['a', 'b', 'c', 'd'],['z','y','x','w']), [(1,'a','z'),(2,'b','y'),(3,'c','x'),(4,'d','w')]),
])


def test_zip(combined, output):
    assert zip.zip_data(*combined) == output