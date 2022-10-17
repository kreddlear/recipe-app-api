"""
Sample tests
"""

from unittest import result

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test that two nums are added together"""
        result = calc.add(5, 6)
        
        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        """Test that numbers are substracted properly"""
        result = calc.subtract(10, 15)

        self.assertEqual(result, 5)
