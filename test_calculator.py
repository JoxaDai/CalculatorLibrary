import calculator

class TestCalculator:
    def test_addition(self):
        calculator = Calculator()
        result = calculator.add(2, 2)
        assert result == 4

    def test_subtraction(self):
        calculator = Calculator()
        result = calculator.subtract(5, 3)
        assert result == 2

    def test_multiplication(self):
        calculator = Calculator()
        result = calculator.multiply(3, 4)
        assert result == 12

    def test_division(self):
        calculator = Calculator()
        result = calculator.divide(10, 2)
        assert result == 5

def test_add():
    calculator = Calculator()
    assert 4 == calculator.add(2, 2)


