list1=[]
list2=[]
list3=[]
n1=int(input(" Enter the total elements: "))
for i in range(n1):
    value=int(input("Enter no : "))
    list1.append(value)
n2=int(input("Enter the total elements: "))
for i in range(n2):
    value=int(input("Enter no : "))
    list2.append(value)
if(n1 == n2):
    print("Same length")
else:
    print("Not same length ")

if(sum(list1)==sum(list2)):
    print("sum is same ")
else:
    print("Sum are different")

list3=[x for x in list1 if x in list2]
print("values occur in both are :",list3)
