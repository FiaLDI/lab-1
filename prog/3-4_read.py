#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_with_readline():
    fileptr = open("file2.txt", "r")
    
    content1 = fileptr.readline()  
    content2 = fileptr.readline()

    print(content1)  
    print(content2)

    fileptr.close()  


def read_with_readlines():
    with open("file2.txt", "r") as fileptr:
        content = fileptr.readlines()  
        print(content)  


def main():
    read_with_readline()
    read_with_readlines()

if __name__ == '__main__':
    main()
        