from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(1, 3)
        self.assertEqual(res, 4)

    def test_subtract_numbers(self):
        res = calc.sub(5, 3)
        self.assertEqual(res, 2)
