from django.test import SimpleTestCase

from d_tools.numbers import generate_number_code_str, generate_number_code_int


class TestOtp(SimpleTestCase):

    def test_generate_number_code_str(self):
        self.assertEqual(len(generate_number_code_str()), 6)
        self.assertEqual(len(generate_number_code_str(num_digits=5)), 5)
        self.assertEqual(type(generate_number_code_str(num_digits=4)), str)

    def test_generate_number_code_int(self):
        self.assertEqual(len(str(generate_number_code_int())), 6)
        self.assertEqual(len(str(generate_number_code_int(num_digits=5))), 5)
        self.assertEqual(type(generate_number_code_int()), int)
