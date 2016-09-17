'''
This file is for optimized versions of the ciphers

'''



import string
english_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                     'y', 'z']



# <------ DONE!!! ------>

# def caesar_cipher(message,shift_value):
#     message = message.lower()
#     ciphered_text = []
#
#     string_punctuation = string.punctuation
#
#     for char in message:
#         if char.isdigit():
#             ciphered_text.append(char)
#
#         elif char in string_punctuation:
#             ciphered_text.append(char)
#
#         elif char in english_alphabets:
#             ciphered_text.append(english_alphabets[(english_alphabets.index(char) + shift_value) % 26])
#
#     return (''.join(ciphered_text))

# <------ DONE!!! ------>

# def caesar_decipher(message, shift_value):
#     message = message.lower()
#     ciphered_text = []
#     string_punctuation = string.punctuation
#
#     for char in message:
#         if char.isdigit():
#             ciphered_text.append(char)
#
#         elif char in string_punctuation:
#             ciphered_text.append(char)
#
#         elif char in english_alphabets:
#             ciphered_text.append(english_alphabets[(english_alphabets.index(
#                 char) - shift_value) % 26])
#
#     return (''.join(ciphered_text))









