'''module for getting alphabet of ascii characters'''
import string

def encode(msg, key):
    result = ''
    alphabet = string.ascii_uppercase

    for i in range(len(msg)):
        result+=alphabet[(alphabet.find(msg[i])+alphabet.find(key[i%len(key)]))%len(alphabet)]
    
    return result
def decode(msg, key):
    result = ''
    alphabet = string.ascii_uppercase

    for i in range(len(msg)):
        result+=alphabet[(alphabet.find(msg[i])+len(alphabet)-alphabet.find(key[i%len(key)]))%len(alphabet)]

    return result

msg = input('Message:')
key = input('Cipher key:')

print('Select mode:')
print('1 - Encode')
print('2 - Decode')
mode = input('Mode: ')
msg = input('Message:')
key = input('Cipher key:')

if mode == '1':
    print(encode(msg, key))
elif mode == '2':
    print(decode(msg, key))
