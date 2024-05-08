import unittest
from unittest.mock import patch, MagicMock
from main import load_dictionary, find_anagrams, get_random_letters, calculate_scrabble_score, find_valid_words

class TestScrabble(unittest.TestCase):
    @patch('main.open')
    def test_load_dictionary(self, mock_open):
        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__iter__.return_value = ['apple', 'banana', 'cherry']
        mock_open.return_value = mock_file

        dictionary = load_dictionary('test.csv')
        self.assertEqual(dictionary, {'apple', 'banana', 'cherry'})

    def test_find_anagrams(self):
        dictionary = {'apple', 'papel', 'pepla'}
        anagrams = find_anagrams('apple', dictionary)
        self.assertEqual(anagrams, ['papel', 'pepla'])

    @patch('main.random.sample')
    def test_get_random_letters(self, mock_sample):
        mock_sample.return_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        letters = get_random_letters()
        self.assertEqual(letters, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    def test_calculate_scrabble_score(self):
        score = calculate_scrabble_score('apple')
        self.assertEqual(score, 9)

    def test_find_valid_words(self):
        random_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        dictionary = {'apple', 'bag', 'cab', 'dab', 'gab'}
        valid_words = find_valid_words(random_letters, dictionary)
        expected_valid_words = [('bag', 6), ('cab', 7), ('dab', 6), ('gab', 6)]
        self.assertEqual(valid_words, expected_valid_words)

if __name__ == "__main__":
    unittest.main()
