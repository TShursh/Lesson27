import unittest
from model.calculator import Calculator


class TestCalculator(unittest.TestCase):
    # AAA
    def test_sum(self):
        # arrange
        a = 10
        b = 20
        expected = 30

        # action
        actual = Calculator.sum(a, b)

        # assert
        assert expected == actual, f"expected {expected}, but was {actual}"

    def test_sub(self):
        a = 10
        b = 7
        expected = 3
        actual = Calculator.sub(a, b)
        if expected != actual:
            self.fail(f"expected {expected}, but was {actual}")

    def test_mul(self):
        a = 8
        b = 7
        expected = 56
        actual = Calculator.mul(a, b)
        self.assertEqual(expected, actual)

    def test_div(self):
        a = 18
        b = 7
        expected = 2
        actual = Calculator.div(a, b)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
