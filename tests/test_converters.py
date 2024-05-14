from django.test import SimpleTestCase

from d_tools.converter import persian_to_english_number


class TestConverters(SimpleTestCase):

    def test_persian_to_english_number(self):
        self.assertEqual(persian_to_english_number("۰۹۳۰۹۹۰"), "0930990")
        self.assertEqual(persian_to_english_number("0۹۳88۹۰"), "0938890")
        self.assertEqual(persian_to_english_number("۰۹۳۰اسب﷼٬hshs۹۹۰"), "0930990")
        self.assertEqual(persian_to_english_number("۰۹۳۰##9۹۰"), "0930990")
