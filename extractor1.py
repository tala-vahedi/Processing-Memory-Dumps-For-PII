# Script Purpose: Process a memory dump and then apply regular expressions to extract e-mail addresses and urls.
# Script Version: 1.0 
# Script Author:  Tala Vahedi

# Script Revision History:
# Version 1.0 Sept 15, 2021, Python 3.x

# 3rd Party Modules
from PIL import Image
# from prettytable import PrettyTable
from binascii import hexlify 

# Python Standard Library
import os
import re

# Psuedo Constants
SCRIPT_NAME    = "Script: Process a memory dump and then apply regular expressions to extract e-mail addresses and urls"
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
    CHUNK_SIZE = 1024

    # regex for email 
    ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}')
    # regex for url
    uPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*') 

    # Create an empty list for emails and urls
    emailList = []
    urlList = []

    # Read in the binary file test.bin
    with open('test.bin', 'rb') as binaryFile:
        while True:
            chunk = binaryFile.read(CHUNK_SIZE)
            if chunk:
                # searching for emails and urls
                emails = ePatt.findall(chunk)
                urls = uPatt.findall(chunk)
                # iterating thru all emails and urls and appending to list
                for eachEmail in emails:
                    emailList.append(eachEmail.decode('UTF-8')) # decoding the string
                for eachURL in urls:
                    urlList.append(eachURL.decode('UTF-8')) # decoding the string
            else:
                break
            
    print("\nPossible e-mails:\n")
    for eachPossibleEmail in emailList:
        print(eachPossibleEmail)
    print()
    print("\nPossible URLs:\n")
    for eachPossibleURL in urlList:
        print(eachPossibleURL)