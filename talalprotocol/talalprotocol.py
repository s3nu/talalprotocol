# -----------------------------------------------------------------------------
# Name: talalprotocol
# Purpose: provide various encryption functions
#
# Author: Talal Khalil
# Start Date: 8/01/2016
# Latest mod: 9/16/2016
#
# Improvements:
# a. non interactive version for direct (add parameters)
# b. extensive debugging required
#
# Notes:
# a. string punctuation needs to be handled
# b. major rewrite for vigenere needed
# c. Add RSA and SHA 256
# -----------------------------------------------------------------------------

'''
This module provides the following encryption functions:


1. Vigenere Cipher
    function calls: vigenere_cipher() or vigenere_decipher()

2. Caesar Cipher
    function calls:
     caesar_cipher(message, shift_value)
     caesar_decipher(message, shift_value)

3. RSA (to be added)

'''

import string
import re

english_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                         'n','o','p','q','r','s','t','u','v','w','x','y','z']



def caesar_cipher(message, shift_value):
    '''
        This function ciphers any submitted message using Caesar Cipher

        Encryption mathematical representation:
        caesar_cipher(x) = (x + n) mod 26
        x: letter index     n: shift value


        Parameters:
        message
        shift value

        Returns:
        ciphered text
        '''
    message = message.lower()
    ciphered_text = []

    for char in message:
        if char.isdigit():
            ciphered_text.append(char)

        elif char in english_alphabets:
            ciphered_text.append(english_alphabets[(english_alphabets.index(
                char) + shift_value) % 26])

    return (''.join(ciphered_text))

def caesar_decipher(message, shift_value):
    '''
    This function ciphers any submitted message using Caesar Cipher

        Encryption mathematical representation:
        caesar_cipher(x) = (x - n) mod 26
        x: letter index     n: shift value


        Parameters:
        message
        shift value

        Returns:
        ciphered text

    '''
    message = message.lower()
    ciphered_text = []
    for char in message:
        if char.isdigit():
            ciphered_text.append(char)

        elif char in english_alphabets:
            ciphered_text.append(english_alphabets[(english_alphabets.index(
                char) - shift_value) % 26])

    return (''.join(ciphered_text))


def vigenere_cipher():
    '''
    This function ciphers any submitted message using Vigenere Cipher

    Encryption mathematical representation:
    vigenere_cipher(y) = (y + k) mod 26
    y: letter index   k: corresponding key letter index

    Parameters:
    N/A (the user will be prompted)
    Returns:
    ciphered text
    '''
    original_text = input('Enter the text you desire to encrypt:')
    original_text = original_text.lower()
    original_text = re.sub(r"\s+","", original_text)
    #print(original_text)

    key_word = input('Enter desired key word for encryption: ')
    key_word = key_word.lower()

    key_list = []
    while key_length < len(original_text):
        for letter in key_word:
            if key_length < len(original_text):
                key_list.append(letter)
                key_length +=1
    #print(key_list)

    encrypted_text_list = []
    index_value = 0
    key_pointer = 0

    for character in original_text:
        if character.isdigit():
            encrypted_text_list.append(character)
        else:
            new_index_value = english_alphabets.index(key_list[key_pointer]) +\
                english_alphabets.index(character)
            if new_index_value > 25:
                new_index_value -= 26
            encrypted_text_list.append(english_alphabets[new_index_value])
            key_pointer +=1
    return (''.join(encrypted_text_list))


def vigenere_decipher():
    '''
    This function deciphers any vigenere_ciphered message

    Parameter:
    N/A (the user will be prompted)
    Returns:
    deciphered message
    '''

    original_text = input('Enter the text you want to decipher: ')
    key_word = input('Enter the shared key word: ')

    key_length = 0
    key_list = []

    while key_length < len(original_text):
        for letter in key_word:
            if key_length < len(original_text):
                key_list.append(letter)
                key_length+=1
    print(key_list)

    decrypted_text_list = []
    index_value = 0
    key_pointer = 0

    for char in original_text:
        if char.isdigit():
            decrypted_text_list.append(char)
        else:
            new_index = english_alphabets.index(char) - \
                        english_alphabets.index(key_list[key_pointer])
            if new_index < 0:
                new_index += 26
            decrypted_text_list.append(english_alphabets[new_index])
            key_pointer +=1
    print(''.join(decrypted_text_list))


def main():
    pass

if __name__ == '__main__':
    main()
