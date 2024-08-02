
i = 1
prev = 2

while True:
    prod = 1
    num = i
    for j in range(2, num):
        if j * j > num: break
        cnt = 0
        while num % j == 0:
            cnt+=1
            num /= j
        prod *= (cnt + 1)
    if num > 1: prod += 1
    if prod > 500:
        print(i)
        break 
    i += prev
    prev+=1