import argparse
import socket
import json
from threading import Thread, Lock
import requests
from bs4 import BeautifulSoup


def work_and_send(k: int, client, stdout_lock):
    url = client.recv(1024)
    sending_data = json.dumps(
        get_top_k_words_by_frequency(url, k)).encode()
    client.sendall(sending_data)
    client.close()
    with stdout_lock:
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


def accept_and_word(sock, sock_lock, k, stdout_lock):
    while True:
        with sock_lock:
            client, _ = sock.accept()
        work_and_send(k, client, stdout_lock)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--workers", type=int, default=4,
                        help="workers count")
    parser.add_argument("-k", type=int, default=3,
                        help="top k words by frequency")
    args = parser.parse_args()

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("localhost", 1234))
    sock.listen(5)

    stdout_lock = Lock()
    sock_lock = Lock()
    for _ in range(int(args.workers)):
        worker = Thread(target=accept_and_word, args=(sock,
                                                      sock_lock,
                                                      args.k,
                                                      stdout_lock))
        worker.start()


if __name__ == "__main__":
    main()
