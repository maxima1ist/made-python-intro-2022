import utils

import time


if __name__ == "__main__":
    statistic = {}

    def statistic_callback(keyword: str):
        if keyword in statistic:
            statistic[keyword] += 1
        else:
            statistic[keyword] = 1

    # unit tests for 'parse_json' function
    utils.parse_json('', keyword_callback=None)

    required_fields = []
    keywords = []
    utils.parse_json('',
                     required_fields, keywords, keyword_callback=statistic_callback)
    assert statistic == {}

    required_fields = ["key2"]
    keywords = ["word1"]
    utils.parse_json('{"key1": "Word1 word2 word2", "key2": "word2 word3"}',
                     required_fields, keywords, keyword_callback=statistic_callback)
    assert statistic == {}

    required_fields = ["key1"]
    keywords = ["word2"]
    utils.parse_json('{"key1": "Word1 word2 word2", "key2": "word2 word3"}',
                     required_fields, keywords, keyword_callback=statistic_callback)
    assert statistic == {"word2": 2}

    statistic = {}
    required_fields = ["key1", "key2", "key3"]
    keywords = ["word1", "word2"]
    utils.parse_json('{"key1": "Word1 word2 word1 word2", "key3": "word2 word3 word1"}',
                     required_fields, keywords, keyword_callback=statistic_callback)
    assert statistic == {"word1": 2, "word2": 3}

    sleep_len = 1.

    @utils.mean(5)
    def foo():
        global sleep_len
        time.sleep(sleep_len)
        sleep_len += 0.1

    # test 'parse_json' function
    for _ in range(10):
        foo()

    print("All tests passed!")
