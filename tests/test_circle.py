import pytest
import math
import source as src

class TestCircle:
    """Class base tests"""

    def setup_method(self, method):
        """This function is run before each test"""
        print(f"Setting up {method}")
        self.circle = src.Circle(10)

    def teardown_method(self, method):
        """This function is run after each test"""
        print(f"Tearing down {method}")
        del self.circle
    
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()