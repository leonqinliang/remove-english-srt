#! /usr/local/bin/python3

import sys
import codecs

def main():
    if len(sys.argv) < 2:
        print ('Please enter a filename.\n')
        sys.exit(1)
    
    filename = sys.argv[1]

    extentionSupported = ['txt', 'srt']

    if filename[-3:].lower() not in extentionSupported:
        print ('Only support TXT and SRT file.\n')
        sys.exit(1)

    try:
        myFile = codecs.open(filename, 'rU', 'utf-8')
    except FileNotFoundError:
        print ('File not found.\n')
        sys.exit(1)

    for line in myFile:
        print (line)

    myFile.close()

if __name__ == '__main__':
    main()