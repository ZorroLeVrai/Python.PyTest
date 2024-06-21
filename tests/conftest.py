import pytest
import source as src

#Make our fixtures definition global to the library

@pytest.fixture
def my_rectangle() -> src.Rectangle:
    return src.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return src.Rectangle(5, 6)