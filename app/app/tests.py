"""
Sample tests for the calc module.
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Tests for the calc module."""

    def test_add_numbers(self):
        """Test adding two numbers together."""
        res = calc.add(5, 7)

        self.assertEqual(res, 12)


class AnotherCalcTests(SimpleTestCase):
    """More tests for the calc module."""

    def test_add_negative_numbers(self):
        """Test adding two negative numbers together."""
        res = calc.add(-3, -6)

        self.assertEqual(res, -9)

    def test_add_random_numbers(self):
        """Test adding two random numbers together."""
        res = calc.add(10, 16)

        self.assertEqual(res, 26)
