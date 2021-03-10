#! usr/bin/env python3
"""Lazily merge iterators into a single iterator"""

import heapq


class MergedIterator(object):
    def __init__(self, *args):
        self.list = heapq.merge(*args)

    def __str__(self):
        return f'{list(self.list)}'


def main():
    iterator_one = iter([0, 0, 1, 2, 3, 4, 5, 6])
    iterator_two = iter([1, 2, 3, 4, 10, 12, 16])
    iterator_three = iter([0, 4, 5, 6, 12, 14, 15, 16])

    merged_iterator = MergedIterator(iterator_one, iterator_two, iterator_three)
    print(str(merged_iterator))


if __name__ == '__main__':
    main()
