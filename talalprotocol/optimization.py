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
string_digits = string.digits



# Decryption needs to be fixed

class BinaryCipher(object):
    '''

    '''

    def __init__(self, message = ''):
        # self.message = message
        # self.message = self.message.lower()
        self.message = message
        self.message = self.message.lower

    def convert_to_binary(self, item1):

        self.binary_value = 0
        digit_list = list(string.digits)
        string_punctuation = list(string.punctuation)

        if item1 in digit_list:
            # added 32 = 0100000 as a flag bit to indicate that a char is a digit
            item1 = int(item1) + 32
            self.binary_value = bin(item1)[2:].zfill(7)
        elif item1 in string_punctuation:
            item1 = string_punctuation.index(item1) + 64
            self.binary_value = bin(item1)[2:].zfill(7)
        else:
            self.binary_value = bin(item1)[2:].zfill(7)

        return self.binary_value


    def BinaryEncryption(self, message):

        self.message = message
        self.message = self.message.lower()
        self.encrypted_message = ''

        for char in self.message:
            if char.isdigit():
                digit_in_binary = self.convert_to_binary(char)
                self.encrypted_message += digit_in_binary
            elif char in string_punctuation:
                punc_in_binary = self.convert_to_binary(char)
                self.encrypted_message += punc_in_binary
            elif char in english_alphabets:
                index = english_alphabets.index(char)
                x = self.convert_to_binary(index)
                self.encrypted_message += x
            else:
                self.encrypted_message += ' '

            self.encrypted_message += ' '

        return self.encrypted_message


    def BinaryDecryption(self, encrypted_message):

        self.encrypted_message = encrypted_message
        self.decrypted_message = ''

        chunks = self.encrypted_message.split(' ')
        print(chunks)
        chunks = [i.strip(' ') for i in chunks]
        print(chunks)

        for i in chunks:
            flag = i[:2]
            if flag == '00':
                index = int(i[2:], 2)
                self.decrypted_message += english_alphabets[index]
            elif flag == '01':
                digit = int(i[2:], 2)
                digit = str(digit)
                self.decrypted_message += digit
            elif flag == '10':
                punctuation_index = int(i[2:], 2)
                self.decrypted_message += string_punctuation[punctuation_index]
            else:
                print('Wrong Input! There is an error! Try again!')
                quit()

        return self.decrypted_message





binary_test = BinaryCipher()
x = binary_test.BinaryEncryption('I am')
print(x)

y = binary_test.BinaryDecryption(x)
print(y)













# my_test = CaesarCipher(3)
#
# x = my_test.encryption('I am Talal')
# print(x)
#
# y = my_test.decryption(x)
# print(y)


# passing_val = '0000000 0100000 1000000 0000000 0100000 1000000'
# x = binary_decryption(passing_val)
# print(x)


# print(string_punctuation)
# message = 'a 1 !'
# ciphered_version = binary_encryption(message)
#
# print(ciphered_version)


# x = caesar_cipher('Hi I am gay',1)
# y = caesar_decipher ('ij j bn',1)
#
# x = vigenere_cipher('My name is talal','math')
# print(x)
#
# y = vigenere_decipher(x, 'math')
# print(y)




