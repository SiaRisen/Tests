import pytest
from YANDEX_API import YaUploader
from unittest import TestCase
from parameterized import parameterized

TOKEN = "..."
uploader = YaUploader(TOKEN)


class TestYandexUT(TestCase):
    """Тестирование с помощью unittest"""

    @classmethod
    def setUpClass(cls):
        print('SetUpClass')

    def setUp(self):
        print('SetUp')

    @parameterized.expand([[
        'New_Folder', 201]])
    def test_get_folder_positiv(self, path, expected):
        status_code = uploader.get_folder(path)
        self.assertEqual(status_code, expected)

    @parameterized.expand([[
        'New_Folder', 409]])
    def test_get_folder_negative(self, path, expected):
        status_code = uploader.get_folder(path)
        self.assertEqual(status_code, expected)

    def tearDown(self):
        print('TearDown')

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')


class TestYandexPT:
    """Тестирование с помощью pytest"""

    # @pytest.mark.parametrize(
    #     "path, expected", ('New_Folder', 201),
    #                       ('New_Folder', 409))
    # def test_get_folder(self, path, expected):
    #     uploader = YaUploader(TOKEN)
    #     result = uploader.get_folder(path)
    #     assert result == expected

    def test_get_folder(self):
        uploader = YaUploader(TOKEN)
        result = uploader.get_folder('New_Folder')
        assert result in (201, 409)
