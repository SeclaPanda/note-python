import math
num = 452022
count = 0
while True:
    sqrtI = round(math.sqrt(num))
    for j in range(2, sqrtI):
        if (num % j) == 0:
            if ((j+num // j) % 7) == 3:
                count += 1
                print (num, '', (j+num) // j)
                break
            else: 
                break
    if count == 5:
        break
    num += 1

    

