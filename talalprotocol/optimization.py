'''
This file is for optimized versions of the ciphers

Goals:

1. All encryptions:
a. need to handle punctuation

2. vigenere:
a. more efficient implementation using modular arithmetic

'''



# non-interactive version
import string
english_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                     'y', 'z']

def caesar_cipher(message,shift_value):
    message = message.lower()
    ciphered_text = []

    for char in message:
        if char.isdigit():
            ciphered_text.append(char)

        elif char in english_alphabets:
            ciphered_text.append(english_alphabets[(english_alphabets.index(char) + shift_value) % 26])

    return (''.join(ciphered_text))

def caesar_decipher(message, shift_value):
    message = message.lower()
    ciphered_text = []

    for char in message:
        if char.isdigit():
            ciphered_text.append(char)

        elif char in english_alphabets:
            ciphered_text.append(english_alphabets[(english_alphabets.index(
                char) - shift_value) % 26])

    return (''.join(ciphered_text))



original_message = 'You are a baaaaar YOLO 1234'
shift_val = 1
x = str(caesar_cipher(original_message,shift_val))
print('The original message is: ' + original_message)
print('The encrypted text is: ' + x)

y = caesar_decipher(x, 1)
print('The decrypted message is: ' + y)







# <------ needs to be optimized ------>
# def vigenere_cipher():
#
#     original_text = input('Enter the text you desire to encrypt: ')
#     original_text = original_text.lower()
#     keyword = input('Enter the encryption key word: ')
#     keyword = list(keyword)
#
#     ciphered_text = []
#
#     for character in original_text:
#         if character.isdigit():
#             ciphered_text.append(character)
#
#         elif character == '':
#             continue
#
#         elif character in english_alphabets:
#             ciphered_text.append(english_alphabets[
#                                      (english_alphabets.index(
#                                          character) + keyword.index()) % 26])
#
#     print(''.join(ciphered_text))



