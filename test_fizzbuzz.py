import unittest

class Fizzbuzz:
    def saidvalue(self, x):
        if x % 15 == 0: return 'fizzbuzz'
        if x % 3 == 0: return 'fizz'
        if x % 5 == 0: return 'buzz'
        return x

    def one_to_100(self):
        for i in range(1,101):
            print saidvalue(i)


class Testing(unittest.TestCase):

    def test_3_returns_fizz(self):
        self.assertEqual(Fizzbuzz().saidvalue(3), 'fizz')
    def test_6_returns_fizz(self):
        self.assertEqual(Fizzbuzz().saidvalue(6), 'fizz')

    def test_5_returns_buzz(self):
        self.assertEqual(Fizzbuzz().saidvalue(5), 'buzz')
    def test_20_returns_buzz(self):
        self.assertEqual(Fizzbuzz().saidvalue(20), 'buzz')

    def test_15_returns_fizzbuzz(self):
        self.assertEqual(Fizzbuzz().saidvalue(15), 'fizzbuzz')
    def test_60_returns_fizzbuzz(self):
        self.assertEqual(Fizzbuzz().saidvalue(60), 'fizzbuzz')

    def test_saidvalue(self):
        self.assertEqual(Fizzbuzz().saidvalue(4), 4)


if __name__ == '__main__':
    unittest.main()
