import unittest

from anagrams import find_anagrams


class FindAnagramsTest(unittest.TestCase):
    def test(self):
        # test empty
        self.assertEqual(find_anagrams("", ""), [])
        self.assertEqual(find_anagrams("some", ""), [])

        # test if pattern is bigger than text
        self.assertEqual(find_anagrams("some text", "some big pettern"), [])

        # random tests
        self.assertEqual(find_anagrams("abc", "d"), [])
        self.assertEqual(find_anagrams("abc", "abc"), [0])
        self.assertEqual(find_anagrams("abcba", "abc"), [0, 2])
        self.assertEqual(find_anagrams("aaa", "a"), [0, 1, 2])
        self.assertEqual(find_anagrams("abc cba xabcd", "abc"), [0, 4, 9])


if __name__ == "__main__":
    unittest.main()
