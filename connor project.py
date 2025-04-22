import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

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
movies = {"Title": [], "Genre": [], "Rating": [], "Status": []}

# functions
def
def
def
def

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

