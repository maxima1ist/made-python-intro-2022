import asyncio
import argparse

import aiohttp


WIKI_PREFIX = "https://en.wikipedia.org/wiki/{number}"


def generate_urls(file_path, count=100):
    lines = []
    for i in range(1, count):
        lines.append(WIKI_PREFIX.format(number=i))
    with open(file_path, "w", encoding="utf-8") as fout:
        fout.write('\n'.join(lines))


async def read_url_in_queue(filename,
                            urls_queue):
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin.readlines():
            line = line.strip()
            if not line:
                continue
            await urls_queue.put(line)


async def fetch_url(url, session):
    async with session.get(url) as resp:
        data = await resp.read()
        print(resp.status, len(data))


async def worker(queue, session):
    while True:
        url = await queue.get()
        try:
            await fetch_url(url, session)
        finally:
            queue.task_done()


async def fetch_batch_urls(urls_queue, workers_count):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(worker(urls_queue, session))
                 for _ in range(workers_count)]

        await urls_queue.join()

        for task in tasks:
            task.cancel()


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", type=int, default=4,
                        help="workers count")
    parser.add_argument("filename", nargs="?", default="urls.txt")
    args = parser.parse_args()

    generate_urls(args.filename)

    urls_queue = asyncio.Queue()
    urls_queue.put_nowait(WIKI_PREFIX.format(number=0))

    tasks = [
        asyncio.create_task(read_url_in_queue(args.filename, urls_queue)),
        asyncio.create_task(fetch_batch_urls(urls_queue, args.count))
    ]

    await urls_queue.join()

    for task in tasks:
        task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
