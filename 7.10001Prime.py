
n = int (1e7 + 10)
sieve = [1] * (n + 10)

list =[]
sieve[0] = 0
sieve[1] = 0
for i in range(2, n):
    if sieve[i]:
            list.append(i)
            
            for j in range(i * i, n, i):
                sieve[j] = 0

print(list[10001])