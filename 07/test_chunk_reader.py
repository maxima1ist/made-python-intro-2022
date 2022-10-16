import io
import unittest
from unittest import mock

from filter_reader import read_if_find


class ReadIfFindTest(unittest.TestCase):
    def test_read_if_find(self):
        fake_file = io.StringIO("Load up on guns, bring your friends\n"
                                "It's fun to lose and to pretend\n"
                                "She's over bored and self assured\n"
                                "Oh no, I know a dirty word\n"
                                "Hello, hello, hello, how low\n"
                                "Hello, hello, hello, how low\n"
                                "Hello, hello, hello, how low\n"
                                "Hello, hello, hello")
        expected_lines = ("Load up on guns, bring your friends",
                          "She's over bored and self assured",
                          "Hello, hello, hello, how low",
                          "Hello, hello, hello, how low",
                          "Hello, hello, hello, how low")
        with mock.patch('filter_reader.open', return_value=fake_file, create=True):
            i_expected = 0
            for finded_line in read_if_find('filename', ["bring", "self", "low"]):
                self.assertEqual(finded_line, expected_lines[i_expected])
                i_expected += 1


if __name__ == "__main__":
    unittest.main()
