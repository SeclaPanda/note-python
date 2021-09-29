a,b,c = map(int, input().split())
q = int(input())
if q == 0:
    print(a * b * c)
else: 
    rule = [input().split() for _ in range(q)]
    print(a, b, c, q, rule)
    
