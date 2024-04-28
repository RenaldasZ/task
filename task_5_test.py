import unittest

def count_lines_with_mistakes(filename):
    """
    Count the number of lines with mistakes in the data.

    This function reads data from a file and counts the number of lines where multiple colors
    are active at the same time or no colors are active.

    Parameters:
        filename (str): The name of the file containing the data.

    Returns:
        int: The total number of lines with mistakes.
    """

    mistakes_count = 0

    with open(filename, 'r') as file:
        next(file)
        
        for line in file:
            red, yellow, green, *_ = map(int, line.strip().split(',')[:3])
            
            # Check if multiple colors are active or no colors are active
            if (red + yellow + green) != 1:
                mistakes_count += 1

    return mistakes_count

class TestCountLinesWithMistakes(unittest.TestCase):
    def test_count_lines_with_mistakes(self):
        self.assertEqual(count_lines_with_mistakes('data.txt'), 671)

if __name__ == '__main__':
    unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.014s

# OK