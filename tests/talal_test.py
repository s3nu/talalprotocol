from talalprotocol.talalprotocol import *

'''
This is just a test file used for
1. testing functionality
2. debugging
'''

#<---------- Caesar testing cases ---------->#

#test case 1
original_message = 'Nadim is .... a faggot bitch ####!'
shift_val = -2
x = str(caesar_cipher(original_message,shift_val))
print('The original message is: ' + original_message)
print('The encrypted text is: ' + x)


#test case 2
a = caesar_decipher(message='I am gay', shift_value=1)
print(a)


#test case 3
my_shift = 2
b = caesar_cipher(message='I am a pansy', my_shift)
print(b)

#test case 4
my_message = 'Imma rob a candy shop REAL QUICKIE !!!!###'
c = caesar_cipher(my_message, shift_value= 4)


#test case 5
d = caesar_cipher()
print(d)


#test case 6
e = caesar_cipher('hi')
print(e)

# test case 7
f = caesar_cipher(1, 'hi')
print(f)





