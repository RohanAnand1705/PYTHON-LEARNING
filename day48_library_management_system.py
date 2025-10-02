class library:
   def __init__(self):
      self.books=[]
      self.number=0
   def add_book(self,book):
      self.books.append(book)
      self.number=len(self.books)

   def count(self):
      return self.number  
   
lib= library()
lib.add_book("1984")
lib.add_book("Hobbit")
print("Number of books:",lib.count())
print("Name of books:",lib.books)