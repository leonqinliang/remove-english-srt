#! /usr/local/bin/python3

import sys
import codecs
import re

def main():
    
    if len(sys.argv) < 3:
        print('Usage: Remove-English-SRT.py <source filename> <target filename>\n')
        sys.exit(1)
    
    sourceFilename = sys.argv[1]
    print ('The source file is:' , sourceFilename)
    
    targetFilename = sys.argv[2]
    print ('The target file is:' , targetFilename)
    
    extentionSupported = ['txt' , 'srt']

    if sourceFilename[-3:].lower() not in extentionSupported:
        print('The source file must be a TXT or SRT file.\n')
        sys.exit(1)

    try:
        sourceFile = codecs.open(sourceFilename, 'rU', 'utf-8')
    except FileNotFoundError:
        print('The source file is not found.\n')
        sys.exit(1)

    try: 
        targetFile = codecs.open(targetFilename, 'w', 'utf-8')
    except FileExistsError:
        print('The target file is already exist.\n')
        sys.exit(1)

    for line in sourceFile:
        firstWord = line[0]
        if not re.search('[a-z , A-Z]' , firstWord):
            targetFile.write(line)
    
    sourceFile.close()
    targetFile.close()

    print ('Job completed.\n')

if __name__ == '__main__':
    main()