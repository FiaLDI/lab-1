#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def pointer():
    with open("file2.txt","r") as fileptr:  
        print("The filepointer is at byte :",fileptr.tell())  
        fileptr.seek(10);  
        print("After reading, the filepointer is at:",fileptr.tell())  
        fileptr.close()


def main():
    pointer()


if __name__ == '__main__':
    main()
        