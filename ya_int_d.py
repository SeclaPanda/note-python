n, m = map(int, input().split())
k = int(input())
a, b, c, d = 0, 0, 0, 0
s_k = [[int(j) for j in input().split()] for _ in range(k)]
for i in range(len(s_k) - 1):
    for j in range(1, len(s_k) - 1):
       a = s_k[i][j] - s_k[i][j + 1]
print(a)