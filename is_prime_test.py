from is_prime import is_prime

import unittest


class IsPrimeTest(unittest.TestCase):
    def testCase1(self):
        self.assertTrue(is_prime(7),  "7 should noot be prime")

    def testCase2(self):
        self.assertFalse(is_prime(8),  "8 should be prime")


if __name__ == '__main__':
    unittest.main()
