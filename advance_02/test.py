import unittest
import filecmp
import os

from server_utils import get_top_k_words_by_frequency
from client_utils import generate_urls

TMP_FILENAME_TXT = "tmp.txt"


class TestTopK(unittest.TestCase):
    def test(self):
        self.assertEqual(get_top_k_words_by_frequency(
            "https://en.wikipedia.org/wiki/Artificial_intelligence", 0
        ), {})
        self.assertEqual(get_top_k_words_by_frequency(
            "https://en.wikipedia.org/wiki/Judo", 3
        ), {"the": 317, "of": 299, "and": 185})
        self.assertEqual(get_top_k_words_by_frequency(
            "https://en.wikipedia.org/wiki/Machine_learning", 7
        ), {"the": 391, "of": 322, "to": 255, "and": 249, "a": 245, "learning": 211, "in": 185})


class TestURLsGenerator(unittest.TestCase):

    def test(self):
        generate_urls(TMP_FILENAME_TXT)
        self.assertTrue(filecmp.cmp("urls.txt", TMP_FILENAME_TXT))
        os.remove(TMP_FILENAME_TXT)


if __name__ == "__main__":
    unittest.main()
