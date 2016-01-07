from itertools import groupby


def groupby_compress(input_str):
    '''
    Given an input string, return a list of tuples with per character counts.
    e.g.: 'aaabbccccd' --> [(3, 'a'), (2, 'b'), (4, 'c'), (1, 'd')]

    Use itertools.groupby() to find groups

    :param input_str: a string to compress
    '''
    char_counts = []
    for k, g in groupby(input_str):
        char_counts.append((len(list(g)), k))
    return char_counts


def iterative_compress(input_str):
    '''
    Given an input string, return a list of tuples with per character counts.
    e.g.: 'aaabbccccd' --> [(3, 'a'), (2, 'b'), (4, 'c'), (1, 'd')]

    :param input_str: a string to compress
    '''
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
