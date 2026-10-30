import unittest

from primes import count_primes, primes_upto


class TestPrimes(unittest.TestCase):
    def test_small(self):
        self.assertEqual(primes_upto(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(primes_upto(1), [])
        self.assertEqual(count_primes(100), 25)


if __name__ == "__main__":
    unittest.main()
