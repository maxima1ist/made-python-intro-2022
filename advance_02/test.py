import os
import time
import filecmp
import unittest
import subprocess

import responses

from server import get_top_k_words_by_frequency
from client import generate_urls

TMP_FILENAME_TXT = "tmp.txt"


class TestTopK(unittest.TestCase):
    @responses.activate
    def test(self):
        ai_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
        responses.add(responses.GET, ai_url, body="", status=200)
        self.assertEqual(get_top_k_words_by_frequency(ai_url, 0), {})

        judo_url = "https://en.wikipedia.org/wiki/Judo"
        responses.add(responses.GET, judo_url,
                      body="some text", status=200)
        self.assertEqual(get_top_k_words_by_frequency(judo_url, 2),
                         {"some": 1, "text": 1})

        ml_url = "https://en.wikipedia.org/wiki/Machine_learning"
        responses.add(responses.GET, ml_url,
                      body="some body once told me the world is gonna roll me", status=200)
        self.assertEqual(get_top_k_words_by_frequency(ml_url, 7),
                         {"body": 1, "me": 2, "once": 1, "some": 1,
                          "the": 1, "told": 1, "world": 1})


class TestURLsGenerator(unittest.TestCase):
    def test(self):
        generate_urls(TMP_FILENAME_TXT)
        self.assertTrue(filecmp.cmp("urls.txt", TMP_FILENAME_TXT))
        os.remove(TMP_FILENAME_TXT)


class TestClientServer(unittest.TestCase):
    CLIENT_TEST_FILE = "client_test.txt"
    CLIENT_TMP_FILE = "client.tmp"

    def test(self):
        server = subprocess.Popen(["python", "server.py"],
                                  stdout=subprocess.DEVNULL)
        time.sleep(1)

        with open(TestClientServer.CLIENT_TMP_FILE, "w", encoding="utf-8") as fout:
            subprocess.run(["python", "client.py"], check=True, stdout=fout)

        server.terminate()

        stats = set()
        with open(TestClientServer.CLIENT_TMP_FILE, encoding="utf-8") as fin:
            for line in fin.readlines():
                stats.add(line)

        real_stats = set()
        with open(TestClientServer.CLIENT_TEST_FILE, encoding="utf-8") as fin:
            for line in fin.readlines():
                real_stats.add(line)

        self.assertEqual(stats, real_stats)

        if os.path.exists(TestClientServer.CLIENT_TMP_FILE):
            os.remove(TestClientServer.CLIENT_TMP_FILE)


if __name__ == "__main__":
    unittest.main()
