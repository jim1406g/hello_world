"""Тесты для city_functions."""

import unittest

from city_functions import get_city_info


class CityTestCase(unittest.TestCase):
    """Тесты для city_functions."""

    def test_get_city_info_city_country(self):
        """Информация для 'omsk' 'russia' выводится правильно ('Omsk, Russia')?"""
        info = get_city_info('omsk', 'russia')
        self.assertEqual(info, 'Omsk, Russia')

    def test_get_city_info_city_country_population(self):
        """Информация для 'omsk' 'russia' '1139897' выводится правильно ('Omsk, Russia - population 1139897')?"""
        info = get_city_info('omsk', 'russia', '1139897')
        self.assertEqual(info, 'Omsk, Russia - population 1139897')


if __name__ == '__main__':
    unittest.main()
