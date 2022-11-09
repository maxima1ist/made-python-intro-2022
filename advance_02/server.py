import argparse
import socket
from threading import Thread, Semaphore

from server_utils import work_and_send

if __name__ == "__main__":
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

    threads = []
    sem = Semaphore(args.workers)
    while True:
        client, addr = sock.accept()
        data = client.recv(1024)
        if not data:
            break
        thread = Thread(target=work_and_send, args=(
            data, args.k, client, sem
        ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
