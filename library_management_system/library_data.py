import json
import os
from books import Book
class Library:
    file_name = "library_books.json"
    def __init__(self):
        self.books_json = []   
        if os.path.exists("library_books.json"):
            with open(self.file_name,"r")as file:
                reader = json.load(file)
                for i in reader:
                    self.books_json.append(i)
            

             
    def add_book(self):
            title = input("enter you book title : ").lower()
            author = input("enter book's auther name : ").lower()
            book_id = int(input("enter book id : "))
            available_book = input("book are available yes or no : ").lower()
            if available_book == "yes":
                available = True
            else:
                available = False

            book1 = Book(title,author,book_id,available)

            title=book1.title
            author =book1.author
            book_id = book1.book_id
            available = book1.available

            dic = {"title":title,"author":author,"book_id":book_id,"available":available}
            self.books_json.append(dic)
            with open(self.file_name , "w") as file:
                json.dump(self.books_json,file)

    def view_books(self):
        self.books = [] 
        with open(self.file_name,"r") as file:
            reader = json.load(file)
            for i in reader:
                    book = Book(
                        i["title"],
                        i["author"],
                        i["book_id"],
                        i["available"]
                        )
                    self.books.append(book)
    
        output=[]
        for book in self.books:
            output.append(
                f"Title : {book.title}\n"
                f"Author : {book.author}\n"
                f"Book ID : {book.book_id}\n"
                f"Available : {book.available}\n"
                f"{'-'*30}"
            )
        
        return "\n" .join(output)

    def search_book(self,info):
        with open(self.file_name,"r") as file:
            reader = json.load(file)
        for i in reader:
            data=str(i["book_id"])
            if data == info or i["title"] == info:
                return (f"Title : {i["title"]}\n"
                        f"Author : {i["author"]}\n"
                        f"Book id : {i["book_id"]}\n"
                        f"Available : {i["available"]}")
            

            
    def borrow_book(self,book_id):
        try:
            with open(self.file_name,"r") as file:
                reader = json.load(file)
            for i in reader:
                if i["book_id"] == book_id and i["available"]==True:
                    i["available"] = False
                    print(f"{i["title"]} book borrow sucessfully ")
                elif i["book_id"] == book_id and i["available"]==False:
                    print(f"{i["title"]} book already borrowed")
            with open(self.file_name,"w")as file:
                json.dump(reader,file)
        except(ValueError):
            print("Enter book id !!")
    
    def return_book(self,book_id):
        try:
            with open(self.file_name,"r") as file:
                reader = json.load(file)
            for i in reader:
                if i["book_id"] == book_id and i["available"] == False: 
                    i["available"] == True
                    print(f"book return sucessfully ")
                elif i["book_id"] == book_id and i["available"]==True:
                    print("you maybe enter the wrong book_id because that book is already alvailable")
        except(ValueError):
            print("Enter book id !!")

            
        with open(self.file_name,"w")as file:
            json.dump(reader,file)
    
    def delete_book(self,book_id):
        try:
            with open(self.file_name,"r") as file:
                reader = json.load(file)
                old_books = []
                yes = False
                
            for alv in reader:
                if alv["book_id"] == book_id:
                    yes = True
                    break
                elif alv["book_id"] != book_id:
                    yes = False
                
            if yes == True:
                for i in reader:
                    if i["book_id"] != book_id:
                        old_books.append(i)
                    else:
                        print("book delete")

                with open(self.file_name,"w")as file:
                    json.dump(old_books,file)  
            
        except(ValueError):
            print("Enter book id !!")
        
            
    if os.path.getsize(file_name) == 0:
        with open("library_books.json" , "w") as file:
            json.dump([],file)

        
    
    
        