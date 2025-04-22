import pickle

def load_from_file():
    try:
        with open("movies.pkl", "rb") as file:
            loaded_movies = pickle.load(file)
            for movie in loaded_movies:
                if isinstance(movie, WatchedMovie):
                    movies["Title"].append(movie.title)
                    movies["Genre"].append(movie.genre)
                    movies["Rating"].append(movie.rating)
                    movies["Status"].append(movie.status)
                elif isinstance(movie, PlannedMovie):
                    movies["Title"].append(movie.title)
                    movies["Genre"].append(movie.genre)
                    movies["Rating"].append(movie.rating)
                    movies["Status"].append(movie.status)
    except FileNotFoundError:
        print("No saved movie list found. Starting with an empty list.")

def save_to_file():
    saved_movies = []
    for i in range(len(movies["Title"])):
        if movies["Status"][i] == "Watched":
            saved_movies.append(WatchedMovie(movies["Title"][i], movies["Genre"][i], movies["Rating"][i]))
        elif movies["Status"][i] == "Planned":
            saved_movies.append(PlannedMovie(movies["Title"][i], movies["Genre"][i]))
    with open("movies.pkl", "wb") as file:
        pickle.dump(saved_movies, file)
    print("Movies saved successfully.")

def add_watched_movie():
    title_value = title.get()
    genre_value = genre.get()
    rating_value = rating.get()
    if title_value and genre_value and rating_value:
        new_movie = WatchedMovie(title_value, genre_value, rating_value)
        movies["Title"].append(new_movie.title)
        movies["Genre"].append(new_movie.genre)
        movies["Rating"].append(new_movie.rating)
        movies["Status"].append(new_movie.status)
        title.set("")
        genre.set("") 
        rating.set("") 
        print(f"Added watched movie: {title_value}")

def add_planned_movie():
    title_value = planned_title.get()
    if title_value:
        new_movie = PlannedMovie(title_value)
        movies["Title"].append(new_movie.title)
        movies["Genre"].append(new_movie.genre)
        movies["Rating"].append(new_movie.rating)
        movies["Status"].append(new_movie.status)
        planned_title.set("") 
        print(f"Added planned movie: {title_value}")
