import unittest
from task_1 import read_color_data, count_color_occurrences

class TestColorOccurrences(unittest.TestCase):
    def setUp(self):
        self.file_path = 'data.txt'

    def test_read_color_data(self):
        color_data = read_color_data(self.file_path)
        self.assertIsInstance(color_data, list)
        self.assertTrue(len(color_data) > 0)

    def test_count_color_occurrences(self):
        color_data = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]
        color_counts = count_color_occurrences(color_data)
        self.assertEqual(color_counts['Red'], 2)
        self.assertEqual(color_counts['Yellow'], 2)
        self.assertEqual(color_counts['Green'], 2)

    def test_count_color_occurrences_no_data(self):
        color_data = []
        color_counts = count_color_occurrences(color_data)
        self.assertEqual(color_counts['Red'], 0)
        self.assertEqual(color_counts['Yellow'], 0)
        self.assertEqual(color_counts['Green'], 0)

    def test_count_color_occurrences_only_red(self):
        color_data = [(1, 0, 0), (1, 0, 0), (1, 0, 0)]
        color_counts = count_color_occurrences(color_data)
        self.assertEqual(color_counts['Red'], 3)
        self.assertEqual(color_counts['Yellow'], 0)
        self.assertEqual(color_counts['Green'], 0)

    def test_count_color_occurrences_only_yellow(self):
        color_data = [(0, 1, 0), (0, 1, 0), (0, 1, 0)]
        color_counts = count_color_occurrences(color_data)
        self.assertEqual(color_counts['Red'], 0)
        self.assertEqual(color_counts['Yellow'], 3)
        self.assertEqual(color_counts['Green'], 0)

    def test_count_color_occurrences_only_green(self):
        color_data = [(0, 0, 1), (0, 0, 1), (0, 0, 1)]
        color_counts = count_color_occurrences(color_data)
        self.assertEqual(color_counts['Red'], 0)
        self.assertEqual(color_counts['Yellow'], 0)
        self.assertEqual(color_counts['Green'], 3)

if __name__ == '__main__':
    unittest.main()
