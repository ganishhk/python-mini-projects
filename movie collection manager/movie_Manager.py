import json
import os
from movie import Movie
class Movie_manager:
    file_name = "movies.json"
    def __init__(self):
        self.movie_collections = []
        self.movie_json = []

    def objects_to_json(self):
        if  len(self.movie_collections) != 0:
            json_data = []
            for i in self.movie_collections:
                dic = {
                    "title" : i.title,
                    "movie_id" : i.movie_id,
                    "genre" : i.genre,
                    "rating" : i.rating,
                    "watched" : i.watched
                }
                json_data.append(dic)
            with open (self.file_name , "w")as file:
                    json.dump(json_data,file)

    def json_to_objects(self):
            for i in self.movie_json:
                movie = Movie(
                    i["title"],
                    i["movie_id"],
                    i["genre"],
                    i["rating"],
                    i["watched"]
                )
                self.movie_collections.append(movie)

    def load_data(self):
        if len(self.movie_json) == 0:
            if os.path.exists(self.file_name):
                with open(self.file_name ,"r") as file:
                    reader = json.load(file)
                    if len(reader) == 0:
                        print(f"{self.file_name} file is empty !!")
                    else:
                        for i in reader:
                            self.movie_json.append(i)
            else:
                with open (self.file_name, "w") as file:
                    json.dump([],file)

    def add_movie(self):
        title = input("enter your movie name that you want to add : ").lower()
        movie_id = int(input("enter your movie id : "))
        genre = input("enter your movie genre : ").lower()
        rating = int(input("whats rating does your movie has out of 10 : "))
        watched_movie = input("have you watched this movie yes or no : ").lower()
        if watched_movie == "yes":
            watched = True
        else:
            watched = False
        movie = Movie(title,movie_id,genre,rating,watched)
        self.movie_collections.append(movie)
        self.save()

    def view(self):
        for i in self.movie_collections:
            print(f"title : {i.title}\n"
                  f"movie id : {i.movie_id}\n"
                  f"genre : {i.genre}\n"
                  f"rating : {i.rating}\n"
                  f"watched : {i.watched}\n"
                  f"{'-'*30}")

    def search(self,info):
        for i in self.movie_collections:
            data = str(i.movie_id)
            if i.title == info or data == info or i.genre == info:
                print (f"title : {i.title}\n"
                        f"movie id : {i.movie_id}\n"
                        f"genre : {i.genre}\n"
                        f"rating : {i.rating}\n"
                        f"watched : {i.watched}\n"
                        f"{'-'*30}")
            return "enter correct input "

    def watched(self,id):
        try:
            for i in self.movie_collections:
                if i.movie_id == id:
                    data = input("have you already watched this movie yes or no : ")
                    if data == "yes":
                        i.watched = True
                        print("done movie watched")
                    else:
                        i.watched = False
                        print("done movie not watched")
            self.save()
        except(ValueError):
            print("enter correct id!!")
            
    def delete(self,id):
        try:
            flag = False
            all_movies = []

            for i in self.movie_collections:
                if i.movie_id == id:
                    flag = True
                    break
                else:
                    flag=False

            if flag == True:
                for i in self.movie_collections:
                    if i.movie_id != id:
                        all_movies.append(i)
                    else:
                        print("movie deleted ")

            self.movie_collections = all_movies
            self.save()
            
        except(ValueError):
            print("enter correct id!!")

    def save(self):
        self.objects_to_json()

            
movie_manager = Movie_manager()
movie_manager.load_data()
movie_manager.json_to_objects()



    
    


