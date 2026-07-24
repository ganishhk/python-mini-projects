from movie_Manager import Movie_manager
movie_manager = Movie_manager()
movie_manager.load_data()
movie_manager.json_to_objects()

def show(value):
    data = value
    if data == "add":
        return movie_manager.add_movie()
    elif data == "search":
        val = input("enter movie id or title or genre to search your movie : ")
        return movie_manager.search(val)
    elif data == "view":
        return movie_manager.view()
    elif data == "delete":
        val=int(input("enter movie id you want to delete : "))
        return movie_manager.delete(val)
    elif data == "watched":
        return movie_manager.watched()

def loop():
    while True:
        action = input("what you want to choose add,search,watched,view,delete or exit : ").lower().strip()

        if action == "exit":
            break
        else:
            data = show(action)
            print(data)
loop()
