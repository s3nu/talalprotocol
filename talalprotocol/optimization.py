'''
This file is for optimized versions of the ciphers

New ciphers mods:

punctuation input
digit input
'''


import string
import re
english_alphabets = list(string.ascii_lowercase)


def linear_search(item,list):
    '''
    This function is an implementation of a linear search algorithm

    Parameters:
    item, list

    Returns:
    the index of the item
    '''
    found = False
    position = 0

    while position < len(list) and not found:
        if list[position] == item:
            index = list.index(item)
            found = True
        else:
            position += 1
    return index


def binary_encryption(message):
    '''
    This encryption algorithm takes the message, acquires its index in the
    alphabets, and finally converts the index to its binary equivalent.
    maximum index = 25
    # of bits required = 6

    For instance:
    message = abc
    index of a = 0, b = 1, c = 1
    encrypted version 000000 000001 000010
    '''

    message = message.lower()

    message = re.sub(r"\s+","", message)
    message = list(message)

    # linear search used to find the char in the alphabets array
    index_list = []
    for char in message:
        index = linear_search(char, message)
        index_list.append(index)
    #print(index_list)





binary_encryption('Drug dealers ANONYMOUS')





