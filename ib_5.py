text = str(input('Введите строку: '))
key1 = str(input('Введите первый ключ в формате: [длина],[ширина] '))
key2 = str(input('Введите второй ключ: '))

m = int(key1.split(',')[0])
n = int(key1.split(',')[1])

if m*n < len(text):
    amount_matrix = len(text) // (m*n)
else:
    amount_matrix = 0

matrix = []
for i in range(amount_matrix + 1):
    matrix.append([])

for i in range(amount_matrix + 1):
    for j in range(n):
        matrix[i].append([''] * m)

k = 0
flag = False
for num in range(amount_matrix + 1):
    for i in range(n):
        for j in range(m):
            matrix[num][i][j] = text[k]
            k += 1
            if k == len(text):
                flag = True
                break
        if flag == True:
            break

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
            if matrix[num][i][j-1] != '':
                encode += matrix[num][i][j-1]

print('Зашифрованная строка: ' + encode)

columns = []
for i in range(amount_matrix + 1):
    columns.append([])

for i in range(amount_matrix + 1):
    for j in range(m):
        columns[i].append('')

min_size = (len(encode) - m * n * amount_matrix) // len(key2)
max_amount = (len(encode) - m * n * amount_matrix) % len(key2)

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
    for j in range(len(key2)):
        for k in range(sizes[i][j]):
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
            decode += dematrix[k][i][j]

print('Расшифрованная строка: ' + decode)