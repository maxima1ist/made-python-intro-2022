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
    def inner_mean(func):
        def wrapper(*args, **kwargs):
            start = timeit.default_timer()
            func(*args, **kwargs)
            end = timeit.default_timer()
            total = round(end - start, 2)
            mean.__k_last_call.append(total)
            if len(mean.__k_last_call) > k:
                mean.__k_last_call.pop(0)
            print("Current time is {} sec. Mean time for {} calls is {} sec.".format(
                total, len(mean.__k_last_call), round(sum(mean.__k_last_call) / len(mean.__k_last_call), 2)))
        return wrapper
    return inner_mean


mean.__k_last_call = []
