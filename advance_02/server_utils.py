import json
from threading import Lock
import requests
from bs4 import BeautifulSoup

lock = Lock()


def work_and_send(url: str, k: int, client, sem):
    with sem:
        sending_data = json.dumps(
            get_top_k_words_by_frequency(url, k)).encode()
        client.sendall(sending_data)
        client.close()
        with lock:
            work_and_send.calls_count += 1
            print(f"Amount of proccesed URLs is {work_and_send.calls_count}")


work_and_send.calls_count = 0


def get_top_k_words_by_frequency(url: str, k: int):
    data = requests.get(url, timeout=5)
    text = data.text
    soup = BeautifulSoup(text, 'html.parser')
    freq_dict = {}
    for word in soup.get_text().split():
        if word not in freq_dict:
            freq_dict[word] = 0
        freq_dict[word] += 1

    res = {}
    for key in sorted(freq_dict, key=freq_dict.get, reverse=True)[:k]:
        res[key] = freq_dict[key]
    return res
