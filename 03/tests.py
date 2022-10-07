import utils

import time


if __name__ == '__main__':
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

    required_fields = ['key2']
    keywords = ['word1']
    utils.parse_json('{'key1': 'Word1 word2 word2', 'key2': 'word2 word3'}',
                     required_fields, keywords, keyword_callback=statistic_callback)
    assert statistic == {}

    required_fields = ['key1']
    keywords = ['word2']
    utils.parse_json('{'key1': 'Word1 word2 word2', 'key2': 'word2 word3'}',
                     required_fields, keywords, keyword_callback=statistic_callback)
    assert statistic == {'word2': 2}

    statistic = {}
    required_fields = ['key1', 'key2', 'key3']
    keywords = ['word1', 'word2']
    utils.parse_json('{'key1': 'Word1 word2 word1 word2', 'key3': 'word2 word3 word1'}',
                     required_fields, keywords, keyword_callback=statistic_callback)
    assert statistic == {'word1': 2, 'word2': 3}

    sleep_len = 0.

    @utils.mean(3)
    def foo():
        global sleep_len
        time.sleep(sleep_len)
        sleep_len += 0.01
        return 'called foo'

    @utils.mean(5)
    def foo_other():
        global sleep_len
        time.sleep(sleep_len)
        sleep_len += 0.01
        return 'called foo_other'

    # test 'parse_json' function
    for _ in range(10):
        assert 'called foo' == foo()
        assert 'called foo_other' == foo_other()

    print('All tests passed!')
