class cosmetics:
    def __init__(self):
        self.prdcode=input("enter the product code")
        self.prdname=input("enter the name of tha product")
        self.fruit=input("enter the name of the fruit")
        self.check=input("whether the fruit present or not(true/false)")
    def getdata(self):
        self.f=input("enter the fruit to be searched")
    def display(self,f):
        if(self.fruit==f and self.check=="true"):
            print("code of the product",self.prdcode)
            print("name of the product",self.prdname)
            print("the fruit present in the product is",self.fruit)
list=[]
for i in range(0,5):
    list.append(cosmetics())
self.f=input("enter the fruit to be searched")
for i in list:
    i.display(f)
    
        

    
        
