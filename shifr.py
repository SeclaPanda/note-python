alp = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ъ', 'э', 'ю', 'я',]
char = ['_', ' ', '*', '!', '?', '.', ',']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

cod = int(input('Сдвиг: '))
shif = input('Что шифруем: ')
answ = []
for i in range(len(shif)):
    for j in range(len(alp)):
        if shif[i] in alp:
            if shif[i] == alp[j]:
                answ.append(alp[(j+cod)])
        j = 0
        if shif[i] in char:
            if shif[i] == char[j]:
                if j+cod >= len(char):
                    j = 0
                    if cod >= 1:
                        j = j + (cod - 1)
                    answ.append(char[j])
                answ.append(char[(j+cod)])
        j = 0
        if shif[i] in num:
            if shif[i] == num[j]:
                answ.append(num[(j+cod)])
        j = 0
print(answ)
#print(''.join(answ))