def indexing(word):
    index = []
    for i in range(len(word)):
        index.append(alphabet.find(word[i]))
    return index

def encode(index_word, index_key):
    dic = {}
    index = 0
    for i in range(len(word)):
        dic[i] = [index_word[i], index_key[index]]
        index += 1
        if index == len(key):
            index = 0
    encode_str = ''
    for i in range(len(word)):
        encode_str += alphabet[(dic[i][0] + dic[i][1]) % len(alphabet)]
    print('Зашифрованная строка: ' + encode_str)
    return encode_str

def decode(index_encode, encode_str):
    dic = {}
    index = 0
    for i in range(len(encode_str)):
        dic[i] = [index_encode[i], index_key[index]]
        index += 1
        if index == len(key):
            index = 0
    decode_str = ''
    for i in range(len(word)):
        decode_str += alphabet[(dic[i][0] - dic[i][1] + len(alphabet)) % len(alphabet)]
    print('Расшифрованная строка: ' + decode_str)

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEраFGHIJKLMNOPQRSTUVWXYZ .,!?-_@"#№$;%^:&*()+=[]{}/<>|0123456789'

word = str(input('Введите слово: '))
key = str(input('Введите ключ: '))

index_word = indexing(word)
index_key = indexing(key)
"encode(index_word, index_key)"
enc_str = encode(index_word, index_key)
index_encode = indexing(enc_str)
decode(index_encode, enc_str)
