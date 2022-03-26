
import unittest
from quantcast_oa import mostFrequent

class UnitTests(unittest.TestCase):

    def testMostFrequent1(self):
        arr = [0, 1, 1, 1, 2, 3]
        return mostFrequent(arr) == 1
    def testMostFrequent2(self):
        arr = [0, 1, 3]
        return mostFrequent(arr) == [0, 1, 3]

if __name__ == '__main__':
    unittest.main()