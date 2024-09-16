class books:
    def __init__(self,title,author,pages):
       self.title=title
       self.author=author
       self.pages=pages

    def title(self):
        return self.title
    
 
    def author(self):
        return self.author
    

    def pages(self):
        return self.pages*2
book1=books("harry potter","jk rowling",3)
print(book1.author())