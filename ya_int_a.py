def change_0(temp):
    i = 0
    j = 1
    temp_0 = [temp[i] - temp[j], temp[1], temp[2]]
    i = 0
    j = 2
    temp_1 = [temp[i] - temp[j], temp[1], temp[2]]
    s0 = sorted(temp_0)
    s1 = sorted(temp_1)
    s2 = sorted(temp)
    return temp_0[0] or temp_1[0] or temp[0] == s0[1] or s1[1] or s2[1]

def change_1(temp):
    i = 1 
    j = 0
    temp_0 = [temp[0], int(temp[i]) - int(temp[j]), temp[2]]
    i = 1
    j = 2
    temp_1 = [temp[0], int(temp[i]) - int(temp[j]), temp[2]]
    s0 = sorted(temp_0)
    s1 = sorted(temp_1)
    s2 = sorted(temp)
    return temp_0[1] == s0[1] or temp_1[1] == s1[1] or temp_0[1] == s2[1] or temp_1[1] == s2[1]

def change_2(temp):
    i = 2
    j = 0
    temp_0 = [temp[0], temp[1], int(temp[i]) - int(temp[j])]
    i = 2
    j = 1
    temp_1 = [temp[0], temp[1], int(temp[i]) - int(temp[j])]
    s0 = sorted(temp_0)
    s1 = sorted(temp_1)
    s2 = sorted(temp)
    return temp_0[2] == s0[1] or temp_1[2] == s1[1] or temp_0[2] == s2[1] or temp_1[2] == s2[1]

def my_median(sample):
    return sorted(sample)[1]

a = [int(i) for i in input().split()]
ch_0 = change_0(a)
ch_1 = change_1(a)
ch_2 = change_2(a)
if ch_0 == True:
    print("YES")
else:
    print("NO")
if ch_1 == True:
    print("YES")
else:
    print("NO")
if ch_2 == True:
    print("YES")
else:
    print("NO")
