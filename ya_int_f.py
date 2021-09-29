n, s, b = map(int, input().split())
branch = input()
branch = branch[::-1]
temp = []
for i in range(len(branch) - 1):
    if branch[i] == branch[i + 1]:
        continue
    if branch[i] == 'S':
        temp.append(s)
    else:
        temp.append(b)
print(temp)