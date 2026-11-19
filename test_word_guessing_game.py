import unittest

from word_guessing_game import is_valid_guess, is_word_guessed, show_progress


class TestHelpers(unittest.TestCase):
    def test_show_progress(self):
        self.assertEqual(show_progress("apple", {"a", "e"}), "a _ _ _ e")

    def test_show_progress_nothing_guessed(self):
        self.assertEqual(show_progress("cat", set()), "_ _ _")

    def test_is_word_guessed_true(self):
        self.assertTrue(is_word_guessed("moon", {"m", "o", "n"}))

    def test_is_word_guessed_false(self):
        self.assertFalse(is_word_guessed("moon", {"m", "o"}))

    def test_valid_guess(self):
        self.assertTrue(is_valid_guess("a"))
        self.assertFalse(is_valid_guess("ab"))
        self.assertFalse(is_valid_guess("1"))
        self.assertFalse(is_valid_guess(""))


if __name__ == "__main__":
    unittest.main()
