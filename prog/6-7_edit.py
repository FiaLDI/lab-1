#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def edit_utf():
    with open("text.txt", "w", encoding="utf-8") as fileptr:
        print(
            "UTF-8 is a variable-width character encoding used for electronic communication.",
            file=fileptr
        )
        print(
            "UTF-8 is capable of encoding all 1,112,064 valid character code points.",
            file=fileptr
        )
        print(
            "In Unicode using one to four one-byte (8-bit) code units.",
            file=fileptr
        )  
        fileptr.close()


def find_sentances():
    with open("text.txt", "r", encoding="utf-8") as fileptr:
       sentences = fileptr.readlines()
       
    for sentence in sentences:
       if ',' in sentence:
           print(sentence)


def main():
    edit_utf()
    find_sentances()


if __name__ == '__main__':
    main()
        