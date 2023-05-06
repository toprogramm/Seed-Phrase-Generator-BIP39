import binascii
import hashlib
import random

def base16_to_base2(base16_number, amount):
    return( f'{int(base16_number, base=16):0>{amount}b}')

#generating entropy and convert to binary
randomBytes = random.randbytes(16).hex()
entropy = base16_to_base2(randomBytes, 128)
WORDLIST = open('english.txt').read().split('\n')
WORDLIST.pop(2048)

def get_hex(binary_number):
    bytes=int(binary_number, 2).to_bytes((len(binary_number) + 7) // 8, byteorder='big')
    hex = binascii.hexlify(hashlib.sha256(bytes).digest()).decode()
    return hex


def binary_seed_phrase():
    tail = get_hex(entropy)[slice(2)]
    
    binary_tail = base16_to_base2(tail, 8)
    binary_full_phrase = entropy + binary_tail
    return binary_full_phrase

def cut_by(value, number_of_elements):
    return [value[i:i + number_of_elements] for i in range(0, len(value) - (len(value) % number_of_elements), number_of_elements)]

array = cut_by(binary_seed_phrase(), 11)
for (index, elem) in enumerate(array):
      array[index] = int(elem, 2)
#from base10 to list with words 
for (index, elem) in enumerate(array):
    array[index] = WORDLIST[array[index]] 

#converting from list to string 
seedPhrase = " ".join(array)
print(seedPhrase)

def cut(value):
    
    for i in value :
      print (i)
#cut(binary_seed_phrase())
#print(len(binary_seed_phrase()))