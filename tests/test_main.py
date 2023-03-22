from unittest import TestCase
from parameterized import parameterized
import pytest

from main import search_ru, get_unique_ids, get_max_value


FIXTURE_1 = [
        ([{'visit1': ['Москва', 'Россия']},
          {'visit2': ['Дели', 'Индия']},
          {'visit3': ['Владимир', 'Россия']},
          {'visit4': ['Лиссабон', 'Португалия']},
          {'visit5': ['Париж', 'Франция']},
          {'visit6': ['Лиссабон', 'Португалия']},
          {'visit7': ['Тула', 'Россия']},
          {'visit8': ['Тула', 'Россия']},
          {'visit9': ['Курск', 'Россия']},
          {'visit10': ['Архангельск', 'Россия']}],
         [
         {'visit1': ['Москва', 'Россия']},
         {'visit3': ['Владимир', 'Россия']},
         {'visit7': ['Тула', 'Россия']},
         {'visit8': ['Тула', 'Россия']},
         {'visit9': ['Курск', 'Россия']},
         {'visit10': ['Архангельск', 'Россия']}
         ])
        ]

FIXTURE_2 = [
             ({'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]},
              [15, 35, 54, 98, 119, 213])
             ]

FIXTURE_3 = [
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98},
     'yandex')
            ]


class TestProgUT(TestCase):
    """Тестирование функций с помощью unittest"""

    @parameterized.expand(FIXTURE_1)
    def test_search_ru1(self, obj, expected):
        # geo_logs = [
        #     {'visit1': ['Москва', 'Россия']},
        #     {'visit2': ['Дели', 'Индия']},
        #     {'visit3': ['Владимир', 'Россия']},
        #     {'visit4': ['Лиссабон', 'Португалия']},
        #     {'visit5': ['Париж', 'Франция']},
        #     {'visit6': ['Лиссабон', 'Португалия']},
        #     {'visit7': ['Тула', 'Россия']},
        #     {'visit8': ['Тула', 'Россия']},
        #     {'visit9': ['Курск', 'Россия']},
        #     {'visit10': ['Архангельск', 'Россия']}
        # ]
        result = search_ru(obj)
        # expected = [
        #     {'visit1': ['Москва', 'Россия']},
        #     {'visit3': ['Владимир', 'Россия']},
        #     {'visit7': ['Тула', 'Россия']},
        #     {'visit8': ['Тула', 'Россия']},
        #     {'visit9': ['Курск', 'Россия']},
        #     {'visit10': ['Архангельск', 'Россия']}
        # ]
        self.assertEqual(result, expected)

    @parameterized.expand(FIXTURE_2)
    def test_get_unique_ids1(self, obj, expected):
        # ids = {'user1': [213, 213, 213, 15, 213],
        #        'user2': [54, 54, 119, 119, 119],
        #        'user3': [213, 98, 98, 35]}

        result = get_unique_ids(obj)
        # expected = [15, 35, 54, 98, 119, 213]
        self.assertEqual(result, expected)

    @parameterized.expand(FIXTURE_3)
    def test_get_max_value1(self, obj, expected):
        # stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

        result = get_max_value(obj)
        # expected = 'yandex'
        self.assertEqual(result, expected)


class TestProgPy:
    """Тестирование функций с помощью pytest"""
    
    def test_search_ru2(self):
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        result = search_ru(geo_logs)
        expected = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        assert result == expected

    def test_get_unique_ids2(self):
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}

        result = get_unique_ids(ids)
        expected = [15, 35, 54, 98, 119, 213]
        assert result == expected

    def test_get_max_value2(self):
        stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

        result = get_max_value(stats)
        expected = 'yandex'
        assert result == expected
