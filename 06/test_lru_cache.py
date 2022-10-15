import unittest

from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_with_default_len(self):
        cache = LRUCache()

        # test empty
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k3"), None)

        # fill values
        for i in range(50):
            cache.set(f"k{i}", f"value{i}")

        # test containing and substitution values
        for i in range(50):
            self.assertEqual(cache.get(f"k{i}"),
                             None if i < 50 - 42 else f"value{i}")

    def test_with_len_2(self):
        cache = LRUCache(2)

        # test empty
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), None)

        # test containing values
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        # test substitution values by circulation frequency
        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")


if __name__ == "__main__":
    unittest.main()
