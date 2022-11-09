import socket
from threading import Lock


WIKI_PREFIX = "https://en.wikipedia.org/wiki/"


def generate_urls(file_path: str, count=100):
    lines = []
    for i in range(count):
        lines.append(WIKI_PREFIX + str(i))
    with open(file_path, "w", encoding="utf-8") as fout:
        fout.write('\n'.join(lines))


lock = Lock()


def send_and_print(url: str, sem):
    with sem:
        sock = socket.socket()
        try:
            sock.connect(("localhost", 1234))
            sock.send(url.encode())
            data = sock.recv(1024).decode("utf-8")
            with lock:
                print(data)
        except ConnectionRefusedError as err:
            print(err)
