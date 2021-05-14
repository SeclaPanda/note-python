import sys

a = int(input())
squ = list(map(int,input().split()))

team = []
i = 0

while i < a:
    b = list(map(int,input().split()))
    team.append(b)
    i += 1

for j in range(len(squ)):
    c = 0
    for c in range(len(squ)):
        if squ[j] >= team[c][0] and squ[j] <= team[c][1]:
            del team[c]
            print('yes', j, c)
            break
        else:
            print('no')
            break
