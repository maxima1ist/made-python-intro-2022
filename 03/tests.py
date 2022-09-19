import utils


if __name__ == "__main__":
    statistic = {}

    def statistic_callback(keyword: str):
        if keyword in statistic:
            statistic[keyword] += 1
        else:
            statistic[keyword] = 1

    # unit tests for 'parse_json' function
    utils.parse_json('', keyword_callback=None)

    required_fields = ["key1"]
    keywords = ["word2"]
    utils.parse_json('{"key1": "Word1 word2 word2", "key2": "word2 word3"}',
                     required_fields, keywords, keyword_callback=statistic_callback)
    assert statistic == {"word2": 2}

    for _ in range(10):
        utils.foo()

    print("All tests passed!")
