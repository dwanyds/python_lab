l=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    num=int(input())
    if(num>100):
        num="over"
    l.append(num)
print(l)
