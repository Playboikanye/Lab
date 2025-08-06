n=int(input("enter maximum range:\n"))
m=int(input("enter minimum range:\n"))
if m%2!=0:
    m=m+1
if n%2!=0:
    n=n-1
res = {num**2 for num in range(m, n,2)}
print(res)