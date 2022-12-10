import argparse
import socket
from threading import Thread, Lock
import time


WIKI_PREFIX = "https://en.wikipedia.org/wiki/"


def generate_urls(file_path: str, count=100):
    lines = []
    for i in range(count):
        lines.append(WIKI_PREFIX + str(i))
    with open(file_path, "w", encoding="utf-8") as fout:
        fout.write('\n'.join(lines))


def read_url_in_queue(file_name: str,
                      urls_queue,
                      queue_lock):
    with open(file_name, "r", encoding="utf-8") as fin:
        for line in fin.readlines():
            line = line.strip()
            if not line:
                continue
            with queue_lock:
                urls_queue.append(line)


def send_and_print(urls_queue, queue_lock, stdout_lock):
    try:
        while True:
            with queue_lock:
                if urls_queue:
                    url = urls_queue[0]
                    urls_queue.pop(0)
                else:
                    queue_lock.release()
                    time.sleep(1)
                    queue_lock.acquire()
                    if urls_queue:
                        continue
                    break

            sock = socket.socket()
            sock.connect(("localhost", 1234))
            sock.send(url.encode())
            data = sock.recv(1024).decode("utf-8")
            with stdout_lock:
                print(data)
    except ConnectionRefusedError as err:
        print(err)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("senders_count", nargs="?", default=4)
    parser.add_argument("file_name", nargs="?", default="urls.txt")
    args = parser.parse_args()

    generate_urls(args.file_name)

    threads = []

    urls_queue = []
    queue_lock = Lock()
    reader = Thread(target=read_url_in_queue, args=(args.file_name,
                                                    urls_queue,
                                                    queue_lock))
    reader.start()
    threads.append(reader)

    stdout_lock = Lock()
    for _ in range(int(args.senders_count)):
        sender = Thread(target=send_and_print, args=(urls_queue,
                                                     queue_lock,
                                                     stdout_lock))
        sender.start()
        threads.append(sender)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
