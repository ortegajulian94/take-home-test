import unittest
from unittest.mock import MagicMock, patch
from haha import get_random_dad_joke, get_random_chuck_norris_joke, get_random_jokes

class TestJokes(unittest.TestCase):
    @patch('haha.requests.get')
    def test_get_random_dad_joke(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'joke': 'Mocked Dad Joke'}
        mock_get.return_value = mock_response

        joke = get_random_dad_joke()
        self.assertEqual(joke, 'Mocked Dad Joke')

    @patch('haha.requests.get')
    def test_get_random_chuck_norris_joke(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'value': 'Mocked Chuck Norris Joke'}
        mock_get.return_value = mock_response

        joke = get_random_chuck_norris_joke()
        self.assertEqual(joke, 'Mocked Chuck Norris Joke')

    @patch('haha.get_random_dad_joke')
    @patch('haha.get_random_chuck_norris_joke')
    def test_get_random_jokes(self, mock_chuck, mock_dad):
        mock_dad.return_value = 'Mocked Dad Joke'
        mock_chuck.return_value = 'Mocked Chuck Norris Joke'

        dad_joke, chuck_joke = get_random_jokes()
        self.assertEqual(dad_joke, 'Mocked Dad Joke')
        self.assertEqual(chuck_joke, 'Mocked Chuck Norris Joke')

if __name__ == "__haha__":
    unittest.main()
