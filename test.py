import unittest
from lottery import generate_output

class LotteryTest(unittest.TestCase):
    # Check if the returned list is of length 10
    def test_length(self):
        output_1 = generate_output()
        self.assertEqual(len(output_1), 10)

    # Check if all balls in random draw are unique
    def test_repeating_balls(self):
        output_2 = generate_output()
        self.assertEqual(len(set(output_2)), len(output_2))

if __name__ == '__main__':
    unittest.main()