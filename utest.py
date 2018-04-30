import unittest

def IsOdd(n):
    return n % 2 == 1

class IsOddTests(unittest.TestCase):
    def testOne(self):
        self.assertTrue(IsOdd(1))
    def testTwo(self):
        self.assertFalse(IsOdd(2))
    def testThree(self):
        self.assertFalse(IsOdd(4))
    def testFour(self):
        self.assertFalse(IsOdd(6))

def main():
    unittest.main()

if __name__ == '__main__':
    main()