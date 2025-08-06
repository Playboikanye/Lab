l1=[]
n=int(input("Enter the number of entries:\n"))
for i in range(n):
    a=int(input("entry:"))
    l1.append(a)

l2=[]
print("The unique elements are\n")
for i in l1:
    if i not in l2:
        print(i)
        l2.append(i)
