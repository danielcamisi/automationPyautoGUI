import unittest
import calc2

class testClac(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calc2.soma(10,10), 20)
        self.assertEqual(calc2.soma(-1,-1), -2)
        self.assertEqual(calc2.soma(6,6), 12)
    def test_menos(self):
        self.assertEqual(calc2.menos(10,10), 0)
        self.assertEqual(calc2.menos(-10,-10), 10)

if __name__ == '__main__':
    unittest.main()