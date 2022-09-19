import json
import time
from datetime import datetime as dt

__k_last_call = []


def parse_json(json_str: str, required_fields=None, keywords=None, *, keyword_callback):
    if not str or not required_fields or not keywords or not keyword_callback:
        return

    json_doc = json.loads(json_str)
    for field in json_doc:
        if field not in required_fields:
            continue
        for word in json_doc[field].split():
            if word not in keywords:
                continue
            keyword_callback(word)


def mean(k):
    def inner_mean(func):
        def wrapper(*args, **kwargs):
            start = dt.now()
            func(*args, **kwargs)
            end = dt.now()
            total = (end - start).microseconds
            __k_last_call.append(total)
            if len(__k_last_call) > k:
                __k_last_call.pop(0)
            print("Mean time for {} calls is {}.".format(
                len(__k_last_call), sum(__k_last_call) / len(__k_last_call)))
        return wrapper
    return inner_mean


@mean(5)
def foo():
    time.sleep(1)
