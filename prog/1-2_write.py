#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def write_file():
    fileptr = open("file2.txt", "w")
    
    fileptr.write(
        "Python is the modern day language. It makes things so simple.\n"
        "It is the fastest-growing programing language"
    )
    
    fileptr.close()


def write_file_different():
    with open("file2.txt", "a") as fileptr:
        fileptr.write(" Python has an easy syntax and user-friendly interaction.")


def main():
    write_file()
    write_file_different()

if __name__ == '__main__':
    main()
        