import pytest
import time
import source as src

def test_add():
    result = src.add(1,4)
    assert result == 5

def test_add_strings():
    result = src.add("Hello", " world")
    assert result == "Hello world"


def test_divide():
    result = src.divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        src.divide(10, 0)


# Add some meta data to the test
@pytest.mark.slow
def test_very_slow():
    time.sleep(1)

#skip test
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert src.add(1,2) == 3

#expect test to fail
@pytest.mark.xfail(reason="We cannot divide by zero")
def test_divide_zero_broken():
    src.divide(4, 0)