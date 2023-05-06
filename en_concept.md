ENGLISH - Translated In Google translate
1. We randomly generate 256 bits - entropy.
! solution in linux
>>tr -dc 0-1 </dev/random | head -c 256 ; echo ''

My python solution - generate 32 bytes => convert to base16 with hex => convert them to binary with 256 character length.

2. Calculate sha256sum in bits mode from entropy
! The solution in linux is
  >> echo entropy | shasum -a 256 -0
3. Get hash - for example c716ada6e8ebd952598bb5622ccbd119620a9ad0ccbcf29ad55077a38603d61b
4. We take the first 2symbols from hash (c7) and translate them into base2
5. Add 2symbols in binary form to the tail of entropy ("entropy + 2symbols")
6. We cut "entropy + 2symbols" by 11 characters into an array (binarySeedPhrase) (24 elements by 11 characters are obtained)
7. Convert each element of binarySeedPhrase to base10
8. Add a dictionary of 2048 words by bip39 is on the github to the array
9. Now we take a list of 2048 words and find them by number from binarySeedPhrase and write them down. should be 24 words.
>> I have this chunks[index] = wordlist[chunks[index]]

10. 12word generator works the same like 24words generator, I change only two values in lines 9-10. 

### 12words
>> randomBytes = random.randbytes(16).hex()
entropy = base16_to_base2(randomBytes, 128)

### 24words 
>>randomBytes = random.randbytes(32).hex()
entropy = base16_to_base2(randomBytes, 256)