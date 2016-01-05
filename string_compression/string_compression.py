from itertools import groupby


def groupby_compress(input_str):
    char_counts = []
    for k, g in groupby(input_str):
        char_counts.append((len(list(g)), k))
    return char_counts


def iterative_compress(input_str):
    target = input_str[0]
    count = 0
    char_counts = []

    for ch in input_str:
        if ch == target:
            count += 1
            continue
        else:
            char_counts.append((count, target))
            target = ch
            count = 1

    char_counts.append((count, target))
    return char_counts
