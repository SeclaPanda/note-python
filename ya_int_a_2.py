def my_median(sample):
    return sorted(sample)[1]

def change1(sample):
    i = 1
    j = 2
    sample = [sample[0], sample[i] - sample[j], sample[2]]
    return sample

def change2(sample):
    i = 1
    j = 0
    sample = [sample[0], sample[i] - sample[j], sample[2]]
    return sample

def change3(sample):
    i = 0
    j = 1
    sample = [sample[i] - sample[j], sample[1], sample[2]]
    return sample

def change4(sample):
    i = 0
    j = 2
    sample = [sample[i] - sample[j], sample[1], sample[2]]
    return sample

def change5(sample):
    i = 2
    j = 0
    sample = [sample[0], sample[1], sample[i] - sample[j]]
    return sample

def change6(sample):
    i = 2
    j = 1
    sample = [sample[0], sample[1], sample[i] - sample[j]]
    return sample

temp = [2, 6, 5]
tempc = temp
a = change1(tempc)

b = change2(tempc)

c = change4(tempc)
d = change3(tempc)
e = change5(tempc)
f = change6(tempc)
med_a = my_median(a)
med_b = my_median(b)
med_c = my_median(c)
med_d = my_median(d)
med_e = my_median(e)
med_f = my_median(f)
med_or = my_median(tempc)

if med_a == temp[0] or med_b == temp[0] or med_c == temp[0] or med_d == temp[0] or med_e == temp[0] or med_f == temp[0] or med_or == temp[0]:
    print('YES')
else:
    print('NO')
if med_a == temp[1] or med_b == temp[1] or med_c == temp[1] or med_d == temp[1] or med_e == temp[1] or med_f == temp[1] or med_or == temp[1]:
    print('YES')
else:
    print('NO')
if med_a == temp[2] or med_b == temp[2] or med_c == temp[2] or med_d == temp[2] or med_e == temp[2] or med_f == temp[2] or med_or == temp[2]:
    print('YES')
else:
    print('NO')

