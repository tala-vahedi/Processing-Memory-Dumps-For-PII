# Script Purpose: Process a memory dump and extract all possible unique strings 5-12 characters in length.
# Script Version: 1.0 
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 Sept 22, 2021, Python 3.x

# 3rd Party Modules
from PIL import Image
from prettytable import PrettyTable
from binascii import hexlify 

# Python Standard Library
import os
import re

# Psuedo Constants
SCRIPT_NAME    = "Script: Process a memory dump and extract all possible unique strings 5-12 characters in length"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Tala Vahedi"

if __name__ == '__main__':
    # Print Basic Script Information
    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()   

    # File Chunk Size
    CHUNK_SIZE = 4096
    wPatt = re.compile(b'[a-zA-Z]{5,15}')

    # Create empty lists
    wordDict = {}

    # Read in the binary file test.bin
    with open('memdump.bin', 'rb') as binaryFile:
        while True:
            chunk = binaryFile.read(CHUNK_SIZE)
            if chunk:
                strings = wPatt.findall(chunk)
                for eachWord in strings:
                    phrase = eachWord.lower()
                    try:
                        value = wordDict[phrase]
                        value += 1
                        wordDict[phrase] = value
                    except:
                        wordDict[phrase] = 1
                    # wordList.append(phrase.decode('UTF-8')) # decoding the string
            else:
                break

    # Setup Pretty Table with the appropriate column names
    pTable = PrettyTable(['Occurances', 'Unique String']) 

    for key, value in wordDict.items():
        pTable.add_row([value, key.decode('UTF-8')])

    print("\nPossible Unique Strings Sorted by Occurances:\n")
    pTable.align = "l"
    # printing out the results sorted by num of occurances 
    print(pTable.get_string(sortby = "Occurances", reversesort = True))