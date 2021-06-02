def make_bit(s):
    out = []
    for i in s:
        out.append("".join(f"{ord(i):08b}"))
    return out


def make_chr(line):
    out = ''
    for i in line:
        out += chr(int(i, base=2))
    return out


text = str(input('Введите строку: '))
key = str(input('Введите ключ: '))

bitText = make_bit(text)
bitKey = make_bit(key)

dic = []
index = 0
for i in range(len(bitText)):
    dic.append([bitText[i], bitKey[index]])
    index += 1
    if index == len(bitKey):
        index = 0

enc = []
for i in range(len(bitText)):
    enc.append(f"{int(dic[i][0], base=2)^int(dic[i][1], base=2):08b}")

encode = make_chr(enc)
print('Зашифрованная строка: ' + encode)

bitEncode = make_bit(encode)
dic = []
index = 0
for i in range(len(bitEncode)):
    dic.append([bitEncode[i], bitKey[index]])
    index += 1
    if index == len(bitKey):
        index = 0

dec = []
for i in range(len(bitEncode)):
    dec.append(f"{int(dic[i][0], base=2)^int(dic[i][1], base=2):08b}")

decode = make_chr(dec)
print('Расшифрованная строка: ' + decode)
