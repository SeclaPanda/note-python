import random
text = str(input('Введите строку: '))
key1 = str(input('Введите первый ключ в формате: [столбцы],[строки] '))
key2 = str(input('Введите второй ключ: '))

m = int(key1.split(',')[0])
n = int(key1.split(',')[1])

key3 = []
for i in range(n):
    key3.append('')

count = 0
for i in range(n):
    for j in range(m):
        key3[i] += str(random.randint(0,1))
        if key3[i][j] == '0':
            count += 1

print('Третий ключ: ' + str(key3))
if m*n - count < len(text):
    amount_matrix = len(text) // ((m*n) - count)
else:
    amount_matrix = 0

matrix = []
for i in range(amount_matrix + 1):
    matrix.append([])

for i in range(amount_matrix + 1):
    for j in range(n):
        matrix[i].append([''] * m)

k = 0
for num in range(amount_matrix + 1):
    for i in range(n):
        for j in range(m):
            if k == len(text):
                break
            if key3[i][j] == '0':
                matrix[num][i][j] = '🚄'
                continue
            elif key3[i][j] == '1':
                matrix[num][i][j] = text[k]
                k += 1


indexing = []
for i in range(amount_matrix + 1):
    indexing.append([])

for i in range(amount_matrix + 1):
    for j in range(len(key2)):
        indexing[i].append('')

for i in range(amount_matrix + 1):
    for j in range(1,len(key2)+1):
        indexing[i][int(key2[j-1]) - 1] = j

encode = ''
for num in range(amount_matrix + 1):
    for j in indexing[num]:
        for i in range(n):
            if matrix[num][i][j-1] != '' and matrix[num][i][j-1] != '🚄':
                encode += matrix[num][i][j-1]

print('Зашифрованная строка: ' + encode)

columns = []
for i in range(amount_matrix + 1):
    columns.append([])

for i in range(amount_matrix + 1):
    for j in range(m):
        columns[i].append('')

remain = len(encode) + (count * amount_matrix) - m * n * amount_matrix

lcount = 0
brcount = 0
for i in range(n):
    for j in range(m):
        if brcount == remain:
            break
        if key3[i][j] == '0':
            lcount += 1
        elif key3[i][j] == '1':
            brcount += 1


min_size = (remain + lcount) // len(key2)
max_amount = (remain + lcount) % len(key2)

sizes = []
for i in range(amount_matrix + 1):
    sizes.append([])

for i in range(amount_matrix + 1):
    for j in range(len(key2)):
        sizes[i].append('')

for i in range(amount_matrix + 1):
    for j in range(len(key2)):
        if i < amount_matrix:
            sizes[i][j] = n
        elif i == amount_matrix:
            if indexing[i][j] <= max_amount:
                sizes[i][j] = min_size + 1
            elif indexing[i][j] > max_amount:
                sizes[i][j] = min_size
num = 0
for i in range(amount_matrix + 1):
    for j in range(m):
        for k in range(sizes[i][j]):
            if key3[k][indexing[i][j] - 1] == '0':
                columns[i][j] += '🚄'
                continue
            elif key3[k][indexing[i][j] - 1] == '1':
                columns[i][j] += encode[num]
                num += 1



dematrix = []
for i in range(amount_matrix + 1):
    dematrix.append([])

for i in range(amount_matrix + 1):
    for j in range(n):
        dematrix[i].append([''] * m)


for k in range(amount_matrix + 1):
    for j in range(len(indexing[k])):
        for i in range(sizes[k][j]):
            if columns[k][j][i] != '':
                dematrix[k][i][indexing[k][j]-1] = columns[k][j][i]

decode = ''
for k in range(amount_matrix + 1):
    for i in range(n):
        for j in range(m):
            if dematrix[k][i][j] != '' and dematrix[k][i][j] != '🚄':
                decode += dematrix[k][i][j]

print('Расшифрованная строка: ' + decode)
