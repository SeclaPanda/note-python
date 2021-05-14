llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
blst = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
clst = [' ', '*', '.', ',', '_', '-', '!', '?']
nlst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
 
 
def encryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            if (ind + shift) >= len(llst):
                shift = shift % len(llst)
                ret += llst[shift - 1]
            else:
                ret += llst[ind+shift]
        elif x in blst:
            ind = blst.index(x)
            if (ind + shift) >= len(blst):
                shift = shift % len(blst)
                ret += blst[shift - 1]
            else:
                ret += blst[ind+shift]
        elif x in clst:
            ind = clst.index(x)
            if (ind + shift) >= len(clst):
                shift = shift % len(clst)
                ret += clst[shift - 1]
            else:
                ret += clst[ind+shift]
        elif x in nlst:
            ind = nlst.index(x)
            if (ind + shift) >= len(nlst):
                shift = shift % len(nlst)
                ret += nlst[shift - 1]
            else:
                ret += nlst[ind+shift]
        else:
            ret += x
    return ret
 
def decryptCaesar(msg, shift):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind-shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind-shift]
        elif x in clst:
            ind = clst.index(x)
            ret += clst[ind-shift]
        elif x in nlst:
            ind = nlst.index(x)
            ret += nlst[ind-shift]
        else:
            ret += x
    return ret
 
chs = int(input("Крипт - 1, декрипт - 2, выход - 3 \n"))
while chs != 3:
    if chs == 1:
        shift = int(input('Сдвиг: '))
        msg = input('Предложение: ')
        print(encryptCaesar(msg, shift))
    if chs == 2:
        shift = int(input('Сдвиг: '))
        msg = input('Предложение: ')
        print(decryptCaesar(msg, shift))
    chs = int(input("Крипт - 1, декрипт - 2, выход - 3 \n"))