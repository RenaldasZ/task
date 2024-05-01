import unittest

def is_complete_cycle(line, next_line, next_next_line, next_next_next_line, next_next_next_next_line):
    colors = line.strip().split(",")[:3]
    next_colors = next_line.strip().split(",")[:3]
    next_next_colors = next_next_line.strip().split(",")[:3]
    next_next_next_colors = next_next_next_line.strip().split(",")[:3]
    next_next_next_next_colors = next_next_next_next_line.strip().split(",")[:3]
    return (colors == ['1', '0', '0'] and
            next_colors == ['0', '1', '0'] and
            next_next_colors == ['0', '0', '1'] and
            next_next_next_colors == ['0', '1', '0'] and
            next_next_next_next_colors == ['1', '0', '0'])

def count_complete_cycles(lines):
    complete_cycles = 0
    for i in range(len(lines)-4):
        if is_complete_cycle(lines[i], lines[i+1], lines[i+2], lines[i+3], lines[i+4]):
            complete_cycles += 1
    return complete_cycles

class TestCompleteCycles(unittest.TestCase):
    def test_is_complete_cycle(self):
        line1 = "1,0,0,7,0:00:07\n"
        line2 = "0,1,0,7,0:00:14\n"
        line3 = "0,0,1,9,0:00:23\n"
        line4 = "0,1,0,1,0:00:24\n"
        line5 = "1,0,0,1,0:00:25\n"

        self.assertTrue(is_complete_cycle(line1, line2, line3, line4, line5))

    def test_count_complete_cycles(self):
        lines = [
            "1,0,0,7,0:00:07\n",
            "0,1,0,7,0:00:14\n",
            "0,0,1,9,0:00:23\n",
            "0,1,0,1,0:00:24\n",
            "1,0,0,1,0:00:25\n",
            "0,1,0,7,0:00:14\n",
            "0,0,1,9,0:00:23\n",
            "0,1,0,1,0:00:24\n",
            "1,0,0,1,0:00:25\n"
        ]

        self.assertEqual(count_complete_cycles(lines), 2)

if __name__ == '__main__':
    unittest.main()
