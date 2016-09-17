from talalprotocol.talalprotocol import *

'''
This is just a test file used for
1. testing functionality
2. debugging
'''


original_message = 'Nadim is .... a faggot bitch ####!'
shift_val = 1
x = str(caesar_cipher(original_message,shift_val))
print('The original message is: ' + original_message)
print('The encrypted text is: ' + x)

y = caesar_decipher(x, 1)
print('The decrypted message is: ' + y)
