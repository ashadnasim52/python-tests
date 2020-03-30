import unittest
import random_game


class TestMain(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = random_game.run_guess(guess, answer)
        self.assertTrue(result)

    def test_wrong_guess(self):
        self.assertFalse(random_game.run_guess(4, 6))

    def test_wrong_number(self):
        self.assertFalse(random_game.run_guess(4, 87))


if __name__ == '__main__':
    unittest.main()
