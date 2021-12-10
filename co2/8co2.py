n=int(input("enter the limit"))
l=[]
m=[]
for i in range(0,n+1):
    w=input("enter the word")
    m.append(len(w))
    l.append(w)
print(l)
print("the length of the longest word is",max(m))
