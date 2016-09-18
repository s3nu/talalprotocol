'''
This file is for new or optimized versions of the ciphers

Binary cipher mods:
handle punctuation and digit inputs
fix output

Note: Binary cipher might be faster if we implement a binary search
'''


import string
import re
english_alphabets = list(string.ascii_lowercase)


def linear_search(item,list):
    '''
    This function is used to find the index of the passed item

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

def converting_to_binary(item1):
    return (bin(item1))






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

    # each item in our list must be converted to its binary equivalent
    binary_cipher = []
    for item in index_list:
        x = converting_to_binary(item)
        binary_cipher.append(x)

    print(''.join(binary_cipher))



binary_encryption('abc')





