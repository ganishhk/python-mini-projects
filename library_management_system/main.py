from library_data import Library
library = Library()
def show_menu(char):
    data = char
    if data == "add":
        return library.add_book()
    elif data =="delete":
        book_id = int(input("enter book id that you want to delete : "))
        return library.delete_book(book_id)
    elif data == "search":
        info =input("enter book id or title of book you want to search : ")
        return library.search_book(info)
    elif data == "borrow":
        book_id = int(input("enter book id that you want to borrow : "))
        return library.borrow_book(book_id)
    elif data == "return":
        book_id = int(input("enter book id that you want to return : "))
        return library.return_book(book_id)
    elif data == "view":
        return library.view_books()
    
def loop():
    while True:
        data = input("what you want to choose add,delete,search,borrow,return,view booksn or exit : ").lower()
        
        if data == "exit":
            break
        
        show = show_menu(data)
        print(show)
loop()

