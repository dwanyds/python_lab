s=lambda a:a*a
r=lambda l,b:l*b
t=lambda b,h:(b*h)/2
a=int(input("enter the side of square"))
l=int(input("enter the length of rectangle"))
b=int(input("enter the breadth"))
h=int(input("enter the height of triangle"))
print("area of square is ",s(a))
print("area of rectangle is ",r(l,b))
print("area of triangle is",t(b,h))
