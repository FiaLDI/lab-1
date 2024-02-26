#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_vowel(letter):
    vowels = "aeiouAEIOU"
    return letter in vowels


def main():
    rezult = ""
    with open("ile2.txt", "r") as fileptr:
        content = fileptr.readline()
        words = content.split()

        for word in words:
            if is_vowel(word[0]):
                rezult += word.lower() + " "
            else:
                rezult += word + " "

    print(rezult)


if __name__ == "__main__":
    main()
