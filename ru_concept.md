1. Генерируем рандомно 256 бит -  entropy.
! Решение в linux 
>>tr -dc 0-1 </dev/random | head -c 256 ; echo ''

Мое решение python - генерируем 32байта => переводим в base16 c помощью hex=> переводим их в двоичное c указанием длины 256символов. 

2. Из entropy вычисляется sha256sum in bits mode 
! Решение в linux такое 
 >> echo entropy | shasum -a 256 -0 
3. Получаем hash - например c716ada6e8ebd952598bb5622ccbd119620a9ad0ccbcf29ad55077a38603d61b
4. Берем первые 2symbols из hash (с7) и переводим их в base2
5. Дописываем 2symbols в бинарном виде в хвост к entropy ("entropy + 2symbols")
6. Режем "entropy + 2symbols" по 11 символов в массив (binarySeedPhrase) (получается 24элемента по 11символов)
7. Переводим каждый элемент binarySeedPhrase в base10
8. Добавляем словарь из 2048слов по bip39 есть на гитхабе в массив
9. Теперь берем список из 2048 слов и находим их по номеру из binarySeedPhrase  и записываем. должно получиться 24слова.
>> У меня это chunks[index] = wordlist[chunks[index]] 
