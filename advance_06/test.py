import os
import unittest
import subprocess

import responses

URLS_FILE = "urls.txt"


class TestAnync(unittest.TestCase):
    TEST_FILE = "test.txt"
    TMP_FILE = "tmp.txt"

    def test(self):
        with open(URLS_FILE, "r", encoding="utf-8") as fin:
            for i, line in enumerate(fin.readlines()):
                line = line.strip()
                responses.add(responses.GET, line, body="ch" * i, status=200)

        with open(TestAnync.TMP_FILE, "w", encoding="utf-8") as fout:
            subprocess.run(["python", "main.py"], check=True, stdout=fout)

        stats = set()
        with open(TestAnync.TMP_FILE, encoding="utf-8") as fin:
            for line in fin.readlines():
                stats.add(line)

        real_stats = set()
        with open(TestAnync.TEST_FILE, encoding="utf-8") as fin:
            for line in fin.readlines():
                real_stats.add(line)

        self.assertEqual(stats, real_stats)

        if os.path.exists(TestAnync.TMP_FILE):
            os.remove(TestAnync.TMP_FILE)


if __name__ == "__main__":
    unittest.main()
