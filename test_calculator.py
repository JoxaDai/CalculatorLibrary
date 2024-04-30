import calculator
class TestCalculator:
 def test_addition():
    calculator = Calculator()
    result = calculator.add(2, 2)
  def test_add():
    assert 4 == calculator.add(2, 2)
