def read_if_find(filename: str, words_to_find: list):
    words_to_find = [word.lower() for word in words_to_find]
    set_of_words_to_find = set(words_to_find)
    with open(filename, encoding="utf-8") as fin:
        for line in fin:
            line = line.rstrip('\n')
            words = [word.lower() for word in line.split()]
            if (set(words) & set_of_words_to_find):
                yield line
