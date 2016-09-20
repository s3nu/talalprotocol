'''
This file is for new or optimized versions of the ciphers

Binary cipher mods:
handle punctuation and digit inputs
fix output

Note: Binary cipher might be faster if we implement a binary search
'''

from talalprotocol import *
import string
import re
english_alphabets = list(string.ascii_lowercase)
string_punctuation = string.punctuation


def linear_search(item, list = english_alphabets):
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

    digit_list = list(string.digits)
    string_punctuation = list(string.punctuation)


    if item1 in digit_list:
        item1 = int(item1)
        binary_value = bin(item1)[2:].zfill(6)
    else:
        binary_value = bin(item1)[2:].zfill(6)

    return binary_value




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
    #print(message)

    # linear search used to find the char in the alphabets array
    string_punctuation = list(string.punctuation)
    index_list = []
    binary_cipher_list = []

    for char in message:

        if char.isdigit():
            digit_in_binary = converting_to_binary(char)
            binary_cipher_list.append(digit_in_binary)

        elif char in string_punctuation:
            binary_cipher_list.append(char)

        else:
            index = linear_search(char)
            index_list.append(index)

    for item in index_list:
        x = converting_to_binary(item)
        binary_cipher_list.append(x)

    print(''.join(binary_cipher_list))


message = 'a123'
print('Original message: '+ message)
print('Encrypted message is: ')
ciphered_version = binary_encryption(message)




# x = caesar_cipher('Hi I am gay',1)
# y = caesar_decipher ('ij j bn',1)
#
# x = vigenere_cipher('My name is talal','math')
# print(x)
#
# y = vigenere_decipher(x, 'math')
# print(y)




