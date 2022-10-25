#create by description https://forum.e4pool.com/viewtopic.php?t=946
#check correct seed phrase on https://iancoleman.io/bip39/
# entropy and sha256 for check converting 
#entropy = '1001000101010011101011111000101011101111011110100001110001001010100100001001011010011100110001001001110100000010000110110001010010111111011001011011011111100001111100000101111110001110010000100010011100001100111000111011100101100110110000011101100101101111'
#binaryHex = c716ada6e8ebd952598bb5622ccbd119620a9ad0ccbcf29ad55077a38603d61b - hex result from ↑ entropy /(binary mode)
#chunks = mule output tired ten peace census drastic squeeze setup trend man city wagon swim march armor mixture bachelor segment shuffle nose genius grant wedding 
import binascii
import hashlib
import random


#generating entropy and convert to binary
randomBytes = random.randbytes(32).hex()
entropy = f'{int(randomBytes, base=16):0>256b}'

#toBytes
h=int(entropy, 2).to_bytes((len(entropy) + 7) // 8, byteorder='big')
#get HEX
binaryHex = binascii.hexlify(hashlib.sha256(h).digest()).decode()

#WORDLIST
f = open('english.txt')     
wordlist = f.read().split('\n')
wordlist.pop(2048)

#get tail and convert to binary
tail = binaryHex[slice(2)]
binaryTail = f'{int("0x"+tail, base=16):0>8b}'

#full seed phrase in binary view
binarySeedPhrase = entropy+binaryTail


#Cut seed phrase into 11 characters
n=11
s=binarySeedPhrase
chunks = [s[i:i + n] for i in range(0, len(s) - (len(s) % n), n)]
#convert to base10
for (index, elem) in enumerate(chunks):
      chunks[index] = int(elem, 2)


#from base10 to list with words 
for (index, elem) in enumerate(chunks):
    chunks[index] = wordlist[chunks[index]] 

#converting from list to string 
seedPhrase = " ".join(chunks)
print(seedPhrase)