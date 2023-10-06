"""Ut for Calculator Library """


import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        assert 2 == calculator.sustract(4, 2)
