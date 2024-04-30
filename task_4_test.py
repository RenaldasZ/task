import unittest
from task_4 import read_color_data, count_correct_cycles

class TestColorSequences(unittest.TestCase):
    def setUp(self):
        self.file_path = 'data.txt'

    def test_read_color_data(self):
        color_sequences = read_color_data(self.file_path)
        self.assertIsInstance(color_sequences, list)
        self.assertTrue(len(color_sequences) > 0)

    def test_count_correct_cycles(self):
        color_sequences = [['Red', 'Yellow', 'Green', 'Yellow', 'Red'], ['Red', 'Yellow', 'Green', 'Yellow', 'Red']]
        correct_cycles = count_correct_cycles(color_sequences)
        self.assertEqual(correct_cycles, 2)

    def test_count_correct_cycles_empty_list(self):
        color_sequences = []
        correct_cycles = count_correct_cycles(color_sequences)
        self.assertEqual(correct_cycles, 0)

    def test_count_correct_cycles_single_sequence(self):
        color_sequences = [['Red', 'Yellow', 'Green', 'Yellow', 'Red', 'Green']]
        correct_cycles = count_correct_cycles(color_sequences)
        self.assertEqual(correct_cycles, 0)

    def test_count_correct_cycles_no_cycles(self):
        color_sequences = [['Red', 'Yellow', 'Green', 'Yellow', 'Green']]
        correct_cycles = count_correct_cycles(color_sequences)
        self.assertEqual(correct_cycles, 0)

if __name__ == '__main__':
    unittest.main()
