#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create_file():
    fileptr = open("newfile.txt", "x")
    print(fileptr)  

    if fileptr:  
        print("File created successfully")

    fileptr.close()  


def main():
    create_file()


if __name__ == '__main__':
    main()
        