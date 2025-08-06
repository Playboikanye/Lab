s1=str(input("enter the string\n"))
l=s1.split()
c=0
dic={}
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[j]==l[j]:
            c+=1
    dic[l[i]]=c
print(dic)
