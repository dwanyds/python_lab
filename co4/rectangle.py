class rectangle:
    def __init__(self):
        self.length=int(input("enter the length"))
        self.breadth=int(input("enter the breadth"))
    def area(self):
        area=self.length*self.breadth
        print("the area is",area)
        return area
    def perimeter(self):
        perimeter=self.length+self.breadth
        print("the perimeter is ",perimeter)
    def display(self):
        print("length is",self.length)
        print("breadth is",self.breadth)
    
obj1=rectangle()
obj2=rectangle()
obj1.display()
obj1.area()
obj1.perimeter()
obj2.display()
obj2.area()
obj2.perimeter()
a1=obj1.area()
a2=obj2.area()
if a1>a2:
    print("area of first rectangle is largest ",a1)
else:
    print("area of second reactangle is largest",a2)
    


     
        
            
