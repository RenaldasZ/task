import unittest
from task_2 import read_color_data, calculate_color_durations
import datetime

class TestColorDurations(unittest.TestCase):
    def setUp(self):
        self.file_path = 'data.txt'

    def test_read_color_data(self):
        color_data = read_color_data(self.file_path)
        self.assertIsInstance(color_data, list)
        self.assertTrue(len(color_data) > 0)

    def test_calculate_color_durations(self):
        color_data = [('1', '0', '0', '3'), ('0', '1', '0', '9'), ('0', '0', '1', '1')]
        color_durations = calculate_color_durations(color_data)
        self.assertEqual(color_durations['Red'], datetime.timedelta(seconds=3))
        self.assertEqual(color_durations['Yellow'], datetime.timedelta(seconds=9))
        self.assertEqual(color_durations['Green'], datetime.timedelta(seconds=1))

    def test_calculate_color_durations_multiple_entries(self):
        color_data = [('1', '0', '0', '3'), ('0', '1', '0', '9'), ('0', '0', '1', '1'), ('1', '0', '0', '4')]
        color_durations = calculate_color_durations(color_data)
        self.assertEqual(color_durations['Red'], datetime.timedelta(seconds=7))
        self.assertEqual(color_durations['Yellow'], datetime.timedelta(seconds=9))
        self.assertEqual(color_durations['Green'], datetime.timedelta(seconds=1))

    def test_calculate_color_durations_empty_data(self):
        color_data = []
        color_durations = calculate_color_durations(color_data)
        self.assertEqual(color_durations['Red'], datetime.timedelta(seconds=0))
        self.assertEqual(color_durations['Yellow'], datetime.timedelta(seconds=0))
        self.assertEqual(color_durations['Green'], datetime.timedelta(seconds=0))

    def test_calculate_color_durations_no_red(self):
        color_data = [('0', '1', '0', '5'), ('0', '0', '1', '2')]
        color_durations = calculate_color_durations(color_data)
        self.assertEqual(color_durations['Red'], datetime.timedelta(seconds=0))
        self.assertEqual(color_durations['Yellow'], datetime.timedelta(seconds=5))
        self.assertEqual(color_durations['Green'], datetime.timedelta(seconds=2))

if __name__ == '__main__':
    unittest.main()
