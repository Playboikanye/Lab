n=int(input("enter the number of elements in the list"))
l=[]

for i in range(0,n,1):
        a=int(input("Enter the 1st number to be entered into the tuple:\n"))
        b=int(input("Enter the 2nd number to be entered into the tuple:\n"))
        l.append((a,b))
temp=[]
for i in range(len(l)):
        for j in range(len(l)-i-1):
                if l[j][1]>l[j+1][1]:
                        temp=l[j]
                        l[j]=l[j+1]
                        l[j+1]=temp

        
print(l)