class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class Book(Publisher):
   
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
      
        self.title=title
        self.author=author
    def display(self):
        print("Name:",self.name)
        print("Title:",self.title)
        print("Author:",self.author)
class Python(Book):
    def __init__(self,name,title,author,price,pages):
        Book.__init__(self,name,title,author)
        self.price=price
        self.pages=pages
    def display(self):
        print("Name:",self.name)
        print("title:",self.title)
        print("author:",self.author)
        print("price:",self.price)
        print("pages:",self.pages)
obj=Publisher('Arun')
obj1=Book('anika','python','Jeeva')
obj2=Python('Arun','python','Jeeva','340','500')
obj.display()
obj1.display()
obj2.display()
