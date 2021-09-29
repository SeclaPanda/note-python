j = input()
s = input()
str1, str2 = list(j), list(s)
count = 0
for x in range(len(str1)):
    ch1 = str1[x]
    if len(str1) > 2 and ch1 == str1[x - 1]:
        continue
    for item in str2:
        ch2 = item
        if ch1 == ch2:
            count += 1
print(count)