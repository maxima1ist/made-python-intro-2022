import argparse
from threading import Thread, Semaphore

from client_utils import generate_urls, send_and_print


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("senders_count", nargs="?", default=4)
    parser.add_argument("file_name", nargs="?", default="urls.txt")
    args = parser.parse_args()

    generate_urls(args.file_name)

    with open(args.file_name, "r", encoding="utf-8") as fin:
        sem = Semaphore(int(args.senders_count))
        threads = []
        for line in fin.readlines():
            line = line.strip()
            if not line:
                continue
            thread = Thread(target=send_and_print, args=(line, sem))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
