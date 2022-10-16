from collections import Counter


def find_anagrams(text: str, pattern: str) -> list[int]:
    res_poses = []

    if len(text) < len(pattern) or not pattern:
        return res_poses

    real_counts = Counter()
    expected_counts = Counter()
    for i, letter in enumerate(pattern):
        real_counts[text[i]] += 1
        expected_counts[letter] += 1

    start = 0
    end = len(pattern) - 1
    while start < len(text) and end < len(text):
        if len(real_counts - expected_counts) == 0:
            res_poses.append(start)

        real_counts[text[start]] -= 1
        start += 1
        end += 1
        if end < len(text):
            real_counts[text[end]] += 1

    return res_poses
