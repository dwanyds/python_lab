l=input("enter the numbers")
s=l.split()
sum=0
for i in range(len(s)):
	s[i]=int(s[i])
	sum=sum+s[i]
print("sum is",sum)
