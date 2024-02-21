#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def main():
    if len(sys.argv) != 2:
        print("Не указан путь!", file=sys.stderr)
        sys.exit(1)

    dictionary = ["it", "seems", "a", "rude"]
    rezult = []
    with open(sys.argv[1], "r") as fileptr:
        content = fileptr.readline()
        words = content.split()

        for word in words:
            if word.lower() not in dictionary:
                rezult.append(word)

    print(rezult)


if __name__ == "__main__":
    main()
    