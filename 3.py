a=[-5,-6,-7,-2,1,2,3,4,-8,5]
b=[x for x in a if x>0]
print(b)
n=int(input("Enter the limit"))
print({x:x**2 for x in range(1,n+1)})
w=input("enter the word")
vowel=["A","E","I","O","U","a","e","i","o","u"]
l=[x for x in w if x in vowel]
print(l)
word=input("enter word")
li=[ord(s) for s in word]
print(li)




