import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 5, 1) == 4

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 9, 1) == 10