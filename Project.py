import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import json

# main class
class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        
# watched movies class
class WatchedMovie(Movie):
    def __init__(self, title, genre, rating):
        super().__init__(title, genre)
        self.rating = rating
        self.status = "Watched"

#planned movies class
class PlannedMovie(Movie):
    def __init__(self, title, genre="Unknown"):
        super().__init__(title, genre)
        self.rating = "N/A"
        self.status = "Planned"

# movies dictionary
movies_dic = {"Title": [], "Genre": [], "Rating": [], "Status": []}

# functions
def add_watched_movie():
    t = title.get()
    g = genre.get()
    try:
        r = float(rating.get())
        if r < 0 or r > 10:
            raise ValueError("Rating must be between 0 and 10")
        movie = WatchedMovie(t, g, r)
        add_to_dict(movie)
        title_entry.delete(0, END) #deletes title from box after its added
        genre_entry.delete(0, END) #deletes genre from box after its added
        rating_entry.delete(0, END) #deletes rating from box after its added
    except ValueError as ve:
        print("Error:", ve)

def add_planned_movie():
    t = planned_title.get()
    movie = PlannedMovie(t)
    add_to_dict(movie)
    planned_title_entry.delete(0, END) #deletes title from box after its added

def add_to_dict(movie):
    movies_dic["Title"].append(movie.title)
    movies_dic["Genre"].append(movie.genre)
    movies_dic["Rating"].append(movie.rating)
    movies_dic["Status"].append(movie.status)

def save_to_file():
    with open("movies.json", "w") as f:
        json.dump(movies_dic, f)

def load_from_file():
    global movies_dic
    try:
        with open("movies.json", "r") as f:
            movies_dic = json.load(f)
        display_loaded_data()
    except FileNotFoundError:
        print("No saved file found.")

def display_loaded_data():
    top = Toplevel(tk)
    top.title("Loaded Movie List")
    text = Text(top, width=60, height=20)
    text.pack()
    for i in range(len(movies_dic["Title"])):
        line = f"{movies_dic['Title'][i]} | Genre: {movies_dic['Genre'][i]} | Rating: {movies_dic['Rating'][i]} | Status: {movies_dic['Status'][i]}"
        text.insert(END, line + "\n")

def show_genre_graph():
    genre_count = {}
    for genre in movies_dic["Genre"]:
        if genre != "Unknown":
            genre_count[genre] = genre_count.get(genre, 0) + 1

    if genre_count:
        plt.bar(genre_count.keys(), genre_count.values())
        plt.title("Movies by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Count")
        plt.show()
    else:
        print("No genres to display.")

def show_status_pie():
    watched = movies_dic["Status"].count("Watched")
    planned = movies_dic["Status"].count("Planned")
    labels = ["Watched", "Planned"]
    sizes = [watched, planned]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Watched vs Planned Movies")
    plt.show()


# gui setup
tk=Tk()
tk.title("Movie List")

frame = ttk.Frame(tk)
frame.grid(column=0,row=0)

# watched movie
title = StringVar()
genre = StringVar()
rating = StringVar()

Label(frame, text="Watched Movie Title:").grid(column=0, row=0)
title_entry = Entry(frame, textvariable=title)
title_entry.grid(column=1, row=0)

Label(frame, text="Genre:").grid(column=0, row=1)
genre_entry = Entry(frame, textvariable=genre)
genre_entry.grid(column=1, row=1)

Label(frame, text="Rating (0-10):").grid(column=0, row=2)
rating_entry = Entry(frame, textvariable=rating)
rating_entry.grid(column=1, row=2)

Button(frame, text="Add Watched", command=add_watched_movie).grid(column=1, row=3)

# planned movie
planned_title = StringVar()

Label(frame, text="Planned Movie Title:").grid(column=3, row=0)
planned_title_entry = Entry(frame, textvariable=planned_title)
planned_title_entry.grid(column=4, row=0)

Button(frame, text="Add Planned", command=add_planned_movie).grid(column=4, row=1)

# file buttons
Button(frame, text="Save List", command=save_to_file).grid(column=1, row=5)
Button(frame, text="Load List", command=load_from_file).grid(column=2, row=5)

# graph buttons
Button(frame, text="Show Genre Graph", command=show_genre_graph).grid(column=1, row=6)
Button(frame, text="Show Status Pie", command=show_status_pie).grid(column=2, row=6)

# quit button
Button(frame, text="Quit", command=tk.destroy).grid(column=4, row=5)
