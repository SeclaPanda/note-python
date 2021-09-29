plit, dobr = map(int, input().split())
plit_a = [int(i) for i in input().split()]
dobr_b = [int(i) for i in input().split()]
count = 0
for i in range(len(plit_a) - 1):
    for j in range(1, len(plit_a) - 1):
        plit_a[i] = plit_a[i] - plit_a[j]
print(plit_a)
'''for item in dobr_b:
    for y in range(len(plit_a)):
        if plit_a[y] != plit_a[-1] and item <= plit_a[y] - plit_a[y + 1]:
            count += 1
        elif item <= plit_a[y]:
            count += 1
        break
if count > dobr:
    print(dobr)
else:
    print(count)
sq = [] * (len(plit_a) - 1)
for i in range(len(plit_a) - 1):
    sq[i] = plit_a[i] - plit_a[i+1] if i != len(plit_a) - 2 else plit_a[i]
print(sq)'''
