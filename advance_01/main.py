import argparse

from lru_cache import LRUCache

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--limit', type=int,
                        help='limit of LRUCache', default=10)
    parser.add_argument('-s', action='store_false',
                        help="show logs in console")
    args = parser.parse_args()

    lru = LRUCache(limit=args.limit, is_log_stdout=args.s)

    print('LRUCache:')
    while True:
        user_input = input('Enter an action: ')

        if user_input == "get":
            key = input('Enter key: ')
            try:
                print(f"Get: {lru.get(int(key))}")
            except ValueError:
                print("You should inter a number!")
        elif user_input == "set":
            try:
                key = input('Enter key: ')
                value = input('Enter value: ')
                lru.set(int(key), int(value))
            except ValueError:
                print("You should inter a number for each of key and value!")
        else:
            print('Invalid input. Supported commands: get, set.')
