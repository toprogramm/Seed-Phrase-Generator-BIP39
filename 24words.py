# create by description https://forum.e4pool.com/viewtopic.php?t=946
# check correct seed phrase on https://iancoleman.io/bip39/
# entropy and sha256 for check converting 
#entropy = '1001000101010011101011111000101011101111011110100001110001001010100100001001011010011100110001001001110100000010000110110001010010111111011001011011011111100001111100000101111110001110010000100010011100001100111000111011100101100110110000011101100101101111'
#hex = c716ada6e8ebd952598bb5622ccbd119620a9ad0ccbcf29ad55077a38603d61b - hex result from ↑ entropy /(binary mode)
#chunks = mule output tired ten peace census drastic squeeze setup trend man city wagon swim march armor mixture bachelor segment shuffle nose genius grant wedding 
import binascii
import hashlib
import random

def base16_to_base2(base16_number, amount):
    return( f'{int(base16_number, base=16):0>{amount}b}')

#generating entropy and convert to binary
randomBytes = random.randbytes(32).hex()
entropy = base16_to_base2(randomBytes, 256)
WORDLIST = open('english.txt').read().split('\n')
WORDLIST.pop(2048)

def get_hex(binary_number):
    bytes=int(binary_number, 2).to_bytes((len(binary_number) + 7) // 8, byteorder='big')
    hex = binascii.hexlify(hashlib.sha256(bytes).digest()).decode()
    return hex


def binary_seed_phrase():
    tail = get_hex(entropy)[slice(2)]
    binary_tail = base16_to_base2(tail, 8)
    binary_full_phrase = entropy+binary_tail
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