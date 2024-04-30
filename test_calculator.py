import calculator
class TestCalculator:
 def test_addition():
    calculator = Calculator()
    result = calculator.add(2, 2)
    assert result == 4
