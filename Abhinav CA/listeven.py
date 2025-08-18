l1=[]
l=list(eval(input("enter a list")))
for i in l:
    if i%2==0:
        l1.append(i)
print("the even numbers of the input list are: ",l1)   
