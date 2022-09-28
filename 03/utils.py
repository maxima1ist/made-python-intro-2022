import json
import timeit


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
    k_last_call = []

    def inner_mean(func):
        def wrapper(*args, **kwargs):
            start = timeit.default_timer()
            res = func(*args, **kwargs)
            end = timeit.default_timer()
            total = round(end - start, 2)

            k_last_call.append(total)
            if len(k_last_call) > k:
                k_last_call.pop(0)

            print("Current time is {} sec. Mean time for {} calls is {} sec.".format(
                total, len(k_last_call),
                round(sum(k_last_call) / len(k_last_call), 3)))

            return res
        return wrapper
    return inner_mean
