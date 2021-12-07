s=input("enter the text")
l=s.split()
d={x:l.count(x) for x in l}
print(d)
