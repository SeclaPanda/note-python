n, m = map(int, input().split())
glass = [[0 for n in range(n)] for nn in range(m)]
for i in range(n - 1):
    for j in range(m - 1):
        glass[i][j] = input().split()
print (glass)