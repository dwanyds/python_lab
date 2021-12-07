N=int(input("Enter the number of name : "))
listf = []
count=0
for i in range(N):
    name = input("Enter name : ")
    listf.append(name)
for i in listf:
    for j in i:
        if(j=="a"):
            count=count+1;
print(count)
