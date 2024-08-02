arr = [1, 2, 2]
n = 3

t = sum(arr)
r = n*(n+1)//2
t2=sum(x**2 for x in arr)
r2=n*(n+1)*(2*n+1)//6
val=(r2-t2)//(r-t)
val2=r-t
print((val+val2)//2,(val-val2)//2)